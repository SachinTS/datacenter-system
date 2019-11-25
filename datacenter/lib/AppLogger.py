import logging
from logging.config import fileConfig
from lib.AppConstants import AppConstants

def get_reporting_logger():
    # print(AppConstants.LOGGING_CONFIG_FILE)
    try:
        fileConfig(AppConstants.LOGGING_CONFIG_FILE,
            disable_existing_loggers=False)
        appllogger = logging.getLogger(AppConstants.LOG_FILE_NAME)
        return appllogger
    except Exception as e:
        print(e)
        print("ERROR: Failed to get the logger %s".format(str(e)))
