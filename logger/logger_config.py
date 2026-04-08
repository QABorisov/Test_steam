import os
import logging


class LoggerConfig:
    LOGGER_DIR_NAME = "logs"
    LOGGER_NAME = "logger"
    LOGS_FILE_NAME = LOGGER_DIR_NAME + os.sep + "test.log"
    LOGS_LEVEL = logging.INFO
    FORMAT = "[%(asctime)s-%(levelname)s]-%(message)s"
    DATATIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
