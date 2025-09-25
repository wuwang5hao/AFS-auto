import configparser
import os
import logging
from logging.handlers import TimedRotatingFileHandler

CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__), "config.ini")  # 示例路径


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


def _write_file(cf):
    """
    工具函数：将修改后的 ConfigParser 对象写入配置文件（私有函数，下划线标识）
    :param cf: 已修改的 configparser.ConfigParser 对象
    """
    try:
        # 以写入模式打开文件，覆盖原有内容（确保修改持久化）
        with open(CONFIG_FILE_PATH, "w", encoding="utf-8") as f:
            cf.write(f)  # ConfigParser 自带的 write 方法，自动格式化配置
        print(f"配置文件写入成功！文件路径：{CONFIG_FILE_PATH}")
    except Exception as e:
        print(f"配置文件写入失败：{e}")
        raise  # 可选：抛出异常，让调用者感知错误


def get_config_value(section, key):
    cf = read_config()
    section_value = cf.get(section, key)
    return section_value


def set_config_value(section, key, value):
    """
    修改配置文件中指定 section 下的 key 对应的 value（若 section 不存在则创建）
    :param section: 配置段名（如 "database"）
    :param key: 配置键名（如 "host"）
    :param value: 要设置的新值（需为字符串，ConfigParser 仅支持字符串值）
    """
    # 1. 读取现有配置
    cf = read_config()

    # 2. 若 section 不存在，先创建该 section（避免 KeyError）
    if not cf.has_section(section):
        cf.add_section(section)
        print(f"配置段 [{section}] 不存在，已自动创建")

    # 3. 修改指定 key 的值（ConfigParser 要求 value 必须是字符串，此处自动转换）
    cf.set(section, key, str(value))  # 转为字符串，避免非字符串值报错

    # 4. 验证修改结果（内存中）
    modified_value = cf.get(section, key)
    print(f"配置修改成功（内存中）：[{section}] {key} = {modified_value}")

    # 5. 关键步骤：调用 _write_file 将修改写入文件（持久化）
    _write_file(cf)


def get_config_port():
    cf = read_config()
    database_port = cf.getint("database", "port")
    return database_port


def init_logger():
    config = read_config()

    # 获取日志配置信息
    log_file = config.get("logging", "log_file")
    log_level = getattr(logging, config.get("logging", "log_level"))
    log_format = config.get("logging", "log_format")

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

