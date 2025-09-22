import configparser
import os
import logging
from logging.handlers import TimedRotatingFileHandler

# 读取配置文件
def read_config():
    # 获取当前文件所在目录
    root_dir = os.path.dirname(os.path.dirname(__file__))
    # 组装config.ini路径，也可以直接写配置文件的具体路径，不用自动获取
    config_dir = os.path.join(root_dir, "common", "config.ini")

    # 创建configparser对象
    cf = configparser.ConfigParser()
    # 读取config.ini
    cf.read(config_dir, encoding="utf-8")
    return cf


def get_config_value(section, key):
    cf = read_config()
    section_value = cf.get(section, key)
    return section_value


def get_config_port():
    cf = read_config()
    database_port = cf.getint("database", "port")
    return database_port


def init_logger():
    config = read_config()

    # 获取日志配置信息
    log_file = config.get('logging', 'log_file')
    log_level = getattr(logging, config.get('logging', 'log_level'))
    log_format = config.get('logging', 'log_format')

    # 创建日志记录器
    logger = logging.getLogger(log_file)
    logger.setLevel(log_level)

    # 避免重复添加处理器
    if not logger.handlers:
        # 创建文件处理器
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)

        # 创建格式化器
        formatter = logging.Formatter(log_format)
        file_handler.setFormatter(formatter)

        # 添加处理器
        logger.addHandler(file_handler)

    return logger

