from logging import FileHandler,Formatter,StreamHandler
from autologging import logged, TRACE, traced
import logging
import sys

logging.basicConfig(
            level=TRACE, filename="log_file.log",filemode='w',
            format="%(asctime)s %(levelname)s:%(filename)s,%(lineno)d:%(name)s.%(funcName)s:%(message)s")

logger = logging.getLogger()
# logger.setLevel(TRACE)
# logger_file = FileHandler("LogFile.log","w")
# format="%(asctime)s : %(levelname)s:%(filename)s,%(lineno)d:%(name)s.%(funcName)s:%(message)s,"
# logger_file.setFormatter(Formatter(format))
# logger.addHandler(logger_file)
#
err_logger = logging.getLogger("error")
format="%(levelname)s:%(filename)s,%(lineno)d:%(name)s.%(funcName)s:%(message)s"
err_logger.setLevel(TRACE)
err_logger_stream = StreamHandler()
err_logger_stream.setLevel(logging.INFO)
err_logger_stream.setFormatter(Formatter(format))
err_logger.addHandler(err_logger_stream)