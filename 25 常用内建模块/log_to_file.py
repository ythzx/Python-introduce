import logging

logging.basicConfig(filename='test.log', level=logging.INFO)
logging.info('started')
logging.info(logging.root.handlers)

