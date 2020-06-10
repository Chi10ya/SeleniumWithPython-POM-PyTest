import inspect
import logging


def customLogger(logLevel=logging.DEBUG):

# Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
# By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("automation.log", mode='a')
    fileHandler.setLevel(logLevel)

# Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%m%d%Y %I:%M:%S %p')

# add formatter to console handler --> chandler
    fileHandler.setFormatter(formatter)

# add console handler to logger
    logger.addHandler(fileHandler)

    return logger
