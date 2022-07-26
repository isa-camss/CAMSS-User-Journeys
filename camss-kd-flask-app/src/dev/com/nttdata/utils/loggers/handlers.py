# -*- coding: utf-8 -*-
import os
from logging.handlers import RotatingFileHandler
from config import constants


class DirFileHandler(RotatingFileHandler):
    """
    Logging handler to create a directory for the logs of the application. Then it generates log files as it was
    configured, following ``RotatingFileHandler`` behaviour.
    """

    def __init__(self, filename, mode='a', max_bytes=0, backup_count=0, encoding=None, delay=False):
        file_log_path = os.path.join(constants.HOME_PATH_LOG, constants.PROJECT_NAME.lower())
        os.makedirs(file_log_path, exist_ok=True)
        log_path = os.path.join(file_log_path, filename)
        RotatingFileHandler.__init__(self, log_path, mode, max_bytes, backup_count, encoding, delay)
