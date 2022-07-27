# -*- coding: utf-8 -*-
import logging.config
from config import constants
import yaml
import os
import com.nttdata.utils.loggers.handlers


def config_logging():
    """
   Configures logging library.
   It loads the YAML file on the project that establishes the different loggers and their handlers.
   :return: None
   """
    with open(os.path.join(constants.BASE_PATH, constants.PROJECT_NAME_FOLDER.lower(), 'config', 'logger', 'logger.yml'),
              'r') as file:
        config = yaml.safe_load(file.read())
        logging.config.dictConfig(config)
