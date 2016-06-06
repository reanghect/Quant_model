import tushare as ts
from util import logger

_data_logger = logger.set_logger("module")


def get_new_data():
    try:
        return ts.get_today_all()
    except ConnectionError as e:
        _data_logger.debug("Can't fetch new data due to Connection Error")
        print(e)
