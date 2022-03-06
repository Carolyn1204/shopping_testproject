import datetime
import logging

from config import global_parameters as gp
from src.common import base

class LogUtil:
    def __init__(self):
        dt = datetime.datetime.now()
        # self.logname = gp.log_path + "mylog_" + dt.strftime() + ".log"
        self.logname = gp.log_path + "mylog_" + base.BaseClass.current_date() + ".log"

    def setMSG(self, level, msg):
        logger = logging.getLogger('roots-online')
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh = logging.FileHandler(self.logname)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        if level == 'debug':
            logger.debug(msg)
        elif level == 'info':
            logger.info(msg)
        elif level == 'warning':
            logger.warning(msg)
        elif level == 'error':
            logger.error(msg)

        logger.removeHandler(fh)
        fh.close()

    def debug(self, msg):
        self.setMSG('debug', msg)

    def info(self, msg):
        self.setMSG('info', msg)

    def warning(self, msg):
        self.setMSG('warning', msg)

    def error(self, msg):
        self.setMSG('error', msg)


if __name__ == '__main__':
    l = LogUtil()
    l.info('test!')
