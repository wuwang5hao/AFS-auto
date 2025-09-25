import pymysql
from pymysql.cursors import DictCursor
from typing import List, Dict, Tuple, Optional
import logging

# 配置日志（可选，用于记录SQL执行与异常）
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("MySQLUtils")


class MySQLUtils:
    def __init__(self, host: str, user: str, password: str, db: str, port: int = 3306, charset: str = "utf8mb4"):
        """
        初始化数据库连接参数（仅存储参数，不立即建立连接）
        :param host: 数据库主机地址
        :param user: 数据库用户名
        :param password: 数据库密码
        :param db: 数据库名称
        :param port: 数据库端口（默认3306）
        :param charset: 字符编码（默认utf8mb4，支持emoji）
        """
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port = port
        self.charset = charset
        # 连接与游标对象（初始化时为None，connect()方法中创建）
        self.connection: Optional[pymysql.connections.Connection] = None
        self.cursor: Optional[pymysql.cursors.DictCursor] = None

    def __enter__(self):
        """
        上下文管理器入口：自动建立数据库连接
        使用with语句时，会自动调用此方法返回工具类实例
        """
        self.connect()
        logger.info("MySQL连接已建立")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        上下文管理器出口：自动关闭连接，处理异常
        :param exc_type: 异常类型（无异常则为None）
        :param exc_val: 异常实例（无异常则为None）
        :param exc_tb: 异常追踪信息（无异常则为None）
        """
        self.close()
        if exc_type:
            logger.error(f"MySQL操作异常: {exc_val} (类型: {exc_type.__name__})")
        else:
            logger.info("MySQL连接已安全关闭")

    def connect(self) -> None:
        """建立数据库连接并创建游标（DictCursor：查询结果返回字典）"""
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                db=self.db,
                port=self.port,
                charset=self.charset,
                cursorclass=DictCursor,  # 关键：结果以{字段名:值}格式返回
                autocommit=False  # 关闭自动提交，手动控制事务
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            # 抛出自定义连接异常，便于上层捕获处理
            raise ConnectionError(f"数据库连接失败: {str(e)}") from e

    def close(self) -> None:
        """关闭游标与连接（避免资源泄漏）"""
        # 先关闭游标，再关闭连接（顺序不可颠倒）
        if self.cursor and not self.cursor.closed:
            self.cursor.close()
            logger.debug("游标已关闭")
        if self.connection and not self.connection._closed:
            self.connection.close()
            logger.debug("连接已关闭")

    def execute(self, sql: str, params: Optional[Tuple] = None) -> int:
        """
        执行增删改操作（INSERT/UPDATE/DELETE）
        :param sql: SQL语句（使用%s作为参数占位符，不可用{}或%）
        :param params: SQL参数（元组格式，如(1, "张三")，防SQL注入）
        :return: 受影响的行数
        """
        if not self.cursor:
            raise RuntimeError("游标未初始化，请先建立数据库连接")

        params = params or ()
        try:
            logger.info(f"执行SQL: {sql} | 参数: {params}")
            rows_affected = self.cursor.execute(sql, params)
            self.connection.commit()  # 提交事务（增删改必须提交）
            logger.info(f"SQL执行成功，受影响行数: {rows_affected}")
            return rows_affected
        except Exception as e:
            self.connection.rollback()  # 异常时回滚事务，避免数据不一致
            raise RuntimeError(f"SQL执行失败: {str(e)} (SQL: {sql}, 参数: {params})") from e

    def query_one(self, sql: str, params: Optional[Tuple] = None) -> Optional[Dict]:
        """
        查询单条记录
        :return: 字典（{字段名:值}），无结果则返回None
        """
        if not self.cursor:
            raise RuntimeError("游标未初始化，请先建立数据库连接")

        params = params or ()
        try:
            logger.info(f"查询SQL: {sql} | 参数: {params}")
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()  # 获取单条结果
            logger.info(f"单条查询结果: {result}")
            return result
        except Exception as e:
            raise RuntimeError(f"查询失败: {str(e)} (SQL: {sql}, 参数: {params})") from e

    def query_all(self, sql: str, params: Optional[Tuple] = None) -> List[Dict]:
        """
        查询多条记录
        :return: 字典列表（[{字段名:值}, ...]），无结果则返回空列表
        """
        if not self.cursor:
            raise RuntimeError("游标未初始化，请先建立数据库连接")

        params = params or ()
        try:
            logger.info(f"批量查询SQL: {sql} | 参数: {params}")
            self.cursor.execute(sql, params)
            results = self.cursor.fetchall()  # 获取所有结果
            logger.info(f"批量查询结果总数: {len(results)}")
            return results
        except Exception as e:
            raise RuntimeError(f"批量查询失败: {str(e)} (SQL: {sql}, 参数: {params})") from e
