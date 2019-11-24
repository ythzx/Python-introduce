import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger('LGESL')
logger.setLevel(level=logging.INFO)
handler = TimedRotatingFileHandler(filename='sync_data.log', when='midnight', interval=1)
handler.suffix = '%Y%m%d'
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("this is info")
