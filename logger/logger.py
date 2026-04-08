import logging
import os
import sys
from logger.logger_config import LoggerConfig


class Logger:
    if not os.path.isdir(LoggerConfig.LOGGER_DIR_NAME):
        os.makedirs(LoggerConfig.LOGGER_DIR_NAME)
    __logger = logging.getLogger(LoggerConfig.LOGGER_NAME)
    __logger.setLevel(LoggerConfig.LOGS_LEVEL)
    __handler1 = logging.FileHandler(LoggerConfig.LOGS_FILE_NAME, mode="w", encoding='utf-8')
    __handler2 = logging.StreamHandler(sys.stdout)
    __formatter = logging.Formatter(LoggerConfig.FORMAT)
    __handler1.setFormatter(__formatter)
    __handler2.setFormatter(__formatter)
    __logger.addHandler(__handler1)
    __logger.addHandler(__handler2)

    @staticmethod
    def set_level(level: str | int) -> None:
        Logger.set_level(level)

    @staticmethod
    def info(message: str) -> None:
        Logger.__logger.info(msg=message)

    @staticmethod
    def debug(message: str) -> None:
        Logger.__logger.debug(msg=message)

    @staticmethod
    def warning(message: str) -> None:
        Logger.__logger.warning(msg=message)

    @staticmethod
    def error(message: str) -> None:
        Logger.__logger.error(msg=message)

    @staticmethod
    def fatal(message: str) -> None:
        Logger.__logger.fatal(msg=message)

    @staticmethod
    def step(message: str) -> None:
        Logger.__logger.step(msg=message)
