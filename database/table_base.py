from database.MySQLUtils import MySQLUtils
from common.Config import get_config_value
from MySQLConfig import productExpressionDay_table_config


# 建表
def create_table(table_config):
    with MySQLUtils(
        host=get_config_value("database", "host"),
        user=get_config_value("database", "write_user"),
        password=get_config_value("database", "write_password"),
        db=get_config_value("database", "database1"),
    ) as db:
        # 2. 在with块内执行操作（与方式1相同）
        try:
            # 创建新表
            table_name = table_config["name"]
            table_comment = table_config.get("comment", "")
            fields = table_config["fields"]

            # 生成字段定义SQL
            field_definitions = []
            for field in fields:
                # 基础字段定义：名称 + 类型
                field_sql = f"`{field['name']}` {field['type']}"

                # 添加约束（如NOT NULL, AUTO_INCREMENT等）
                if "constraints" in field:
                    field_sql += " " + " ".join(field["constraints"])

                # 添加注释
                if "comment" in field:
                    field_sql += f" COMMENT '{field['comment']}'"

                field_definitions.append(field_sql)

            create_table_sql = f"""
                        CREATE TABLE IF NOT EXISTS `{table_name}` (
                            {', '.join(field_definitions)},
                            PRIMARY KEY (`{table_config['primary_key']}`)  # 主键单独指定，更灵活
                        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='{table_comment}';
                        """
            rows = db.execute(create_table_sql)
            print(f"更新成功，影响行数：{rows}")
            print(create_table_sql)

        except Exception as e:
            print(f"操作失败：{e}")

    # 3. 退出with块后，自动调用__exit__关闭连接（无需手动处理）
    print("连接已自动关闭")


create_table(productExpressionDay_table_config)
