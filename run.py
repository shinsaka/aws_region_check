import logging
import logging.config
import settings
import datetime


logging.config.dictConfig(settings.LOGGING_CONFIG)
logger = logging.getLogger(__name__)


def main():
    from lib import pricing
    from lib import s3
    from lib import utils

    logger.info('start')

    # get last region list from file on S3
    last_regions = s3.download(
        settings.UPLOAD_S3_BUCKET,
        settings.UPLOAD_S3_PREFIX + settings.UPLOAD_S3_CURRENT)

    # get region list from Pricelist API
    regions = pricing.get_union_regions()

    # upload(current)
    s3.upload(
        settings.UPLOAD_S3_BUCKET,
        settings.UPLOAD_S3_PREFIX + settings.UPLOAD_S3_CURRENT,
        regions)

    # upload(history)
    s3.upload(
        settings.UPLOAD_S3_BUCKET,
        '{}{}-regionlist.txt'.format(
            settings.UPLOAD_S3_PREFIX,
            datetime.date.today().strftime('%Y%m%d')),
        regions)

    # diff
    (added, removed) = utils.diff_lists(last_regions, regions)

    logger.info('added:{}'.format(added))
    logger.info('removed:{}'.format(removed))

    logger.info('end')


if __name__ == '__main__':
    main()
