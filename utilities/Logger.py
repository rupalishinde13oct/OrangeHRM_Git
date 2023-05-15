import inspect
import logging


class LegGenrator:

    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)

        logFile = logging.FileHandler("E:\\OrangeHRM\\Logs\\OrangeHRM.log")
        logFormate = logging.Formatter(" %(asctime)s : %(levelname)s : %(funcName)s : %(lineno)s : %(message)s")

        logFile.setFormatter(logFormate)

        logger.addHandler(logFile)
        logger.setLevel(logging.INFO)
        return logger