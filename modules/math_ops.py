from utils import logger

logger = logger._get_logger()

def _add(x: int, y: int):
    result = x + y
    logger.info(f'{x} + {y} = {result}')
    return result

def _sub(x: int, y: int):
    result = x - y
    logger.info(f'{x} - {y} = {result}')
    return result

def _mul(x: int, y: int):
    result = x * y
    logger.info(f'{x} * {y} = {result}')
    return result

def _div(x: int, y: int):
    try:
        result = x / y
    except ZeroDivisionError as ex:
        logger.error(str(ex))
        return None
    else:
        logger.info(f'{x} / {y} = {result}')
        return result
