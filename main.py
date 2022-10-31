import logging
import logging.handlers
from logging.handlers import SysLogHandler

logger = logging.getLogger('myLogger')

logger.setLevel(logging.DEBUG)



handler = SysLogHandler(facility=SysLogHandler.LOG_DAEMON, address='/dev/log')
logger.addHandler(handler)

logger.debug('Fooo!')

