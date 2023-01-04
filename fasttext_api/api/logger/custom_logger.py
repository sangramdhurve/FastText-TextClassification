import inspect
import logging


class CustLogger:
    def custlogger(self, loglevel=logging.INFO):
        # Set class/method name from where it called
        logger_name = inspect.stack()[1][3]

        # Create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(loglevel)

        # Create console handler or file handler and set the log level
        file_name = logging.FileHandler("text_api.log")

        # Create formatter - how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S')

        # Add formatter to console or file handler
        file_name.setFormatter(formatter)

        # Add console handler to logger
        logger.addHandler(file_name)
        return logger