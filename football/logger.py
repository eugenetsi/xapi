import logging

"""
Logging Levels:

Level       When it’s used
_____       ______________

DEBUG       Detailed information, typically of interest only when 
            diagnosing problems.

INFO        Confirmation that things are working as expected.

WARNING     An indication that something unexpected happened, or indicative 
            of some problem in the near future (e.g. ‘disk space low’). 
            The software is still working as expected.

ERROR       Due to a more serious problem, the software has not been able 
            to perform some function.

CRITICAL    A serious error, indicating that the program itself may be unable 
            to continue running.
"""

# to monitor in real time the log file, run: tail -f log.log

def setup_logger(logger_name, log_file, level=logging.DEBUG):
    logger = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(module)s:%(funcName)s: %(message)s', datefmt='%Y:%m:%d::%H:%M:%S')
    #formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(module)s:%(name)s:%(funcName)s: %(message)s', datefmt='%Y:%m:%d::%H:%M:%S')
    fileHandler = logging.FileHandler(log_file, mode='a')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    logger.setLevel(level)
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)

    return logger
