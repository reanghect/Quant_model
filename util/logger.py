import logging
import logging.config

__author__ = 'Will Chen'

CONF_LOG = "/home/perpy/Project/Quant_model/conf/logging.conf"
logging.config.fileConfig(CONF_LOG, defaults={'logfilename': 'data.log'})


def set_logger(name=None):
    logger = logging.getLogger(name)
    return logger
