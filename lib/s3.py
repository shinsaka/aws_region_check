import io
import logging
import boto3


logger = logging.getLogger(__name__)


def upload(bucket_name, key_name, data):
    """
    upload to s3
    """
    with io.BytesIO() as fp:
        for r in data:
            fp.write(r.encode())
        fp.seek(0)

        s3 = boto3.client('s3')
        logger.info('start upload to s3:{}/{}'.format(bucket_name, key_name))
        s3.upload_fileobj(fp, bucket_name, key_name)
        logger.info('end upload to s3:{}/{}'.format(bucket_name, key_name))


def download(bucket_name, key_name):
    """
    get sorted list form s3 object
    """
    with io.BytesIO() as fp:
        s3 = boto3.client('s3')
        s3.download_fileobj(bucket_name, key_name, fp)
        fp.seek(0)

        return sorted([x.decode() for x in fp.readlines()])
