import os
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
if bool(os.environ.get('DEBUG', False)):
    logger.setLevel(logging.DEBUG)
