from database.MySQLUtils import MySQLUtils
from common.Config import get_config_value


# def query_user():
#     # 1. 创建类实例（传入数据库连接参数）
#     db = MySQLUtils(
#         host=get_config_value("database", "host"),
#         user=get_config_value("database", "write_user"),
#         password=get_config_value("database", "write_password"),
#         db=get_config_value("database", "database1"),
#     )
#
#     try:
#         # 2. 建立连接
#         db.connect()
#
#         # 3. 执行操作（示例）
#         # 3.1 查询单条记录
#         user = db.query_one("SELECT * FROM amz_test WHERE id = %s", (1,))
#         print("查询单条结果：", user)  # 输出格式：{'id': 1, 'name': 'xxx', ...}
#
#         # 3.2 查询多条记录
#         all_users = db.query_all("SELECT * FROM amz_test LIMIT 5")
#         print("查询多条结果：", all_users)  # 输出格式：[{'id':1, ...}, {'id':2, ...}, ...]
#
#         # # 3.3 执行增删改
#         # # 示例：插入一条记录
#         # rows = db.execute(
#         #     "INSERT INTO users (name, email) VALUES (%s, %s)",
#         #     ("张三", "zhangsan@example.com"),
#         # )
#         # print(f"插入成功，影响行数：{rows}")
#
#     except Exception as e:
#         print(f"操作失败：{e}")
#     finally:
#         # 4. 手动关闭连接（必须执行，避免资源泄漏）
#         db.close()
#
#
# query_user()

# print(get_config_value("database", "host"))
# 1. 用with语句创建实例（自动调用__enter__建立连接）
with MySQLUtils(
    host=get_config_value("database", "host"),
    user=get_config_value("database", "write_user"),
    password=get_config_value("database", "write_password"),
    db=get_config_value("database", "database1"),
) as db:
    # 2. 在with块内执行操作（与方式1相同）
    try:
        # 查询
        user = db.query_one("SELECT * FROM amz_test WHERE id = %s", (2,))
        print("查询结果：", user)

        # 更新
        rows = db.execute("UPDATE amz_test SET num = %s WHERE name = %s", (25, "大黄2"))
        print(f"更新成功，影响行数：{rows}")

    except Exception as e:
        print(f"操作失败：{e}")

# 3. 退出with块后，自动调用__exit__关闭连接（无需手动处理）
print("连接已自动关闭")

# print(get_config_value("database", "database1"))
# print(MySQLUtils)
#
#
# def query_user(user_id):
#     """查询用户信息的示例函数"""
#     try:
#         # 1. 用with语句创建实例（自动连接和关闭）
#         with MySQLUtils(
#             host=get_config_value("database", "host"),  # 从配置获取host
#             user=get_config_value("database", "write_user"),  # 用户名
#             password=get_config_value("database", "write_password"),  # 密码
#             db=get_config_value("database", "database1")  # 数据库名
#         ) as db:  # db是MySQLUtils的实例
#
#             # 2. 执行查询
#             user = db.query_one(
#                 "SELECT * FROM amz_test WHERE id = %s",  # SQL语句
#                 (user_id,)  # 参数（元组格式，防SQL注入）
#             )
#
#             if user:
#                 print(f"查询到用户：{user}")
#                 return user
#             else:
#                 print(f"未找到ID为{user_id}的用户")
#                 return None
#
#     except Exception as e:
#         print(f"数据库操作失败：{e}")
#         return None
#
# query_user(2)
# # # 测试调用
# # if __name__ == "__main__":
# #     query_user(1001)  # 查询ID为1001的用户
