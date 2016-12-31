import os
import logging
from logging.handlers import TimedRotatingFileHandler

__version__  = '0.0.1'
__author__ = "borisliu"


class DailyRotatingFileHandler(TimedRotatingFileHandler):
    """
    File logger that will rotate every daily midnight.
    
    """
    def __init__(self, filename, formatter = logging.Formatter('%(asctime)s,%(message)s', '%Y-%m-%d %H:%M:%S')):
        """ 
        Just Copied from logging.handlers.TimedRotatingFileHandler
        # filename : the base logging file name,etc '/var/log/httpd/access.log'.
        # formatter : the logger's formatter, default is logging.Formatter(
    '%(asctime)s,%(message)s', '%Y-%m-%d %H:%M:%S').
        # level : the logger's level, default is logging.DEBUG
        """
        TimedRotatingFileHandler.__init__(self, filename=loggerFile, when='midnight', encoding='utf-8')
        suffix = '%Y%m%d'
        setFormatter(formatter)
