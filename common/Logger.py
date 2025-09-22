import logging
import os
from logging.handlers import TimedRotatingFileHandler


def _setup_logger():
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log")
    os.makedirs(log_dir, exist_ok=True)

    log_path = os.path.join(log_dir, "app.log")

    logger = logging.getLogger("app_logger")
    if logger.handlers:  # 避免重复初始化
        return logger

    logger.setLevel(logging.INFO)

    # 文件 handler
    file_handler = TimedRotatingFileHandler(
        log_path,
        when="midnight",  # 每天 0 点切分
        interval=1,  # 间隔 1 天
        backupCount=90,  # 保留 90 天的日志，超过会自动删除
        encoding="utf-8",
    )
    file_handler.suffix = "%Y-%m-%d"

    # 自定义归档文件名：app_2025-08-22.log
    def custom_namer(default_name):
        """
        默认: log/app.log.2025-08-22
        修改后: log/app_2025-08-22.log
        """
        dirname, basename = os.path.split(default_name)  # log/, app.log.2025-08-22
        parts = basename.split(".")  # ['app', 'log', '2025-08-22']
        if len(parts) >= 3:
            filename = f"{parts[0]}_{parts[-1]}.log"
            return os.path.join(dirname, filename)
        return default_name

    file_handler.namer = custom_namer

    formatter = logging.Formatter("%(asctime)s [%(levelname)s] [%(name)s] %(message)s")
    file_handler.setFormatter(formatter)

    # 控制台 handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# 单例 logger
logger = _setup_logger()
