# 创建数据表完全可配置

# 日产品表现
productExpressionDay_table_config = {
    "name": "users",
    "comment": "用户基本信息表",
    "primary_key": "user_id",  # 主键字段名
    "fields": [
        {
            "name": "user_id",
            "type": "INT",
            "constraints": ["AUTO_INCREMENT", "NOT NULL"],
            "comment": "用户的唯一标识符"
        },
        {
            "name": "username",
            "type": "VARCHAR(100)",
            "constraints": ["NOT NULL"],
            "comment": "用户的昵称"
        },
        {
            "name": "email",
            "type": "VARCHAR(255)",
            "constraints": ["UNIQUE", "NOT NULL"],
            "comment": "用户的邮箱地址"
        },
        {
            "name": "created_at",
            "type": "TIMESTAMP",
            "constraints": ["DEFAULT CURRENT_TIMESTAMP"],
            "comment": "用户注册时间"
        }
    ]
}
}