import logging
import logging.config

__author__ = 'Will Chen'

CONF_LOG = "../conf/logger.conf"
logging.config.fileConfig(CONF_LOG)


def set_logger(name=None):
    logger = logging.getLogger(name)
    return logger
