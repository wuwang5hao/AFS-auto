# import pymysql
#
#
# def Connection():
#     try:
#         db = pymysql.connect(host="192.168.12.25", user="remote_admin", password="maY89Zjm", database="amazon")
#         print('数据库连接成功!')
#     except pymysql.Error as e:
#         print('数据库连接失败' + str(e))
#     finally:
#         db.close()
#
#
# Connection()
import pymysql
from common.Config import get_config_value
import logging


# def Insert():
#     db = pymysql.connect(host="192.168.12.25", user="remote_admin", password="maY89Zjm", database="amazon")
#     cur = db.cursor()
#     sqlQuery = " INSERT INTO amz_test (name, num, money) VALUE (%s,%s,%s) "
#     value = ("大黄", 20, 2.35)
#     try:
#         cur.execute(sqlQuery, value)
#         db.commit()
#         print('数据插入成功！')
#     except pymysql.Error as error:
#         print("数据插入失败：" + str(error))
#         db.rollback()
#     finally:
#         db.close()
#
#
# Insert()


def Find():
    # # 1. 从配置文件读取参数
    # host = get_config_value("database", "host")
    # user = get_config_value("database", "write_user")
    # password = get_config_value("database", "write_password")
    # db_name = get_config_value("database", "database1")
    #
    # # 2. 打印出所有参数及其类型
    # print("--- 从配置文件读取的参数 ---")
    # print(f"host: '{host}' (类型: {type(host)})")
    # print(f"user: '{user}' (类型: {type(user)})")
    # print(f"password: '{password}' (类型: {type(password)})")
    # print(f"db: '{db_name}' (类型: {type(db_name)})")
    # print("--------------------------")
    #
    # # 3. 检查参数是否为空
    # if not all([host, user, password, db_name]):
    #     print("错误：从配置文件读取的参数中存在空值，请检查配置文件。")
    #     return

    db = pymysql.connect(
        host=get_config_value("database", "host"),
        user=get_config_value("database", "write_user"),
        password=get_config_value("database", "write_password"),
        db=get_config_value("database", "database1"),
    )
    cur = db.cursor()
    sqlQuery = "SELECT * FROM amz_test"
    try:
        cur.execute(sqlQuery)
        results = cur.fetchall()
        for row in results:
            print(row)
    except pymysql.Error as e:
        print("数据查询失败：" + str(e))
    finally:
        db.close()


def add():
    db = pymysql.connect(
        host="192.168.12.25",
        user="write_user2",
        password="QyHXM20Z",
        database="amazon",
    )
    cur = db.cursor()
    sqlAdd = "INSERt INTO amz_test (name,numbers) VALUES (%s,%s)"
    data = [("大黄f", 123)]
    cur.executemany(sqlAdd, data)
    db.commit()
    db.close()


def create():
    db = pymysql.connect(
        host="192.168.12.25",
        user="write_user2",
        password="QyHXM20Z",
        database="amazon",
    )
    cur = db.cursor()

    # SQL语句
    sql = """
    CREATE TABLE `employees` (
      `employee_id` int NOT NULL AUTO_INCREMENT,
      `first_name` varchar(14) NOT NULL,
      `last_name` varchar(16) NOT NULL,
      `hire_date` date COMMENT'用户的昵称',
      PRIMARY KEY (`employee_id`)
    ) ENGINE=InnoDB
"""
    cur.execute(sql)
    db.commit()
    db.close()


Find()
