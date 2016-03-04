import calendar
import croniter

from datetime import datetime
import logging

from rq.utils import ColorizingStreamHandler


# from_unix from times.from_unix()
def from_unix(string):
    """Convert a unix timestamp into a utc datetime"""
    return datetime.utcfromtimestamp(float(string))


# to_unix from times.to_unix()
def to_unix(dt):
    """Converts a datetime object to unixtime"""
    return calendar.timegm(dt.utctimetuple())


def get_next_scheduled_time(cron_string):
    """Calculate the next scheduled time by creating a crontab object
    with a cron string"""
    itr = croniter.croniter(cron_string, datetime.utcnow())
    return itr.get_next(datetime)


def setup_loghandlers(level='INFO'):
    logger = logging.getLogger('rq_scheduler.scheduler')
    if not logger.handlers:
        logger.setLevel(level)
        formatter = logging.Formatter(fmt='%(asctime)s %(message)s',
                                      datefmt='%H:%M:%S')
        handler = ColorizingStreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
