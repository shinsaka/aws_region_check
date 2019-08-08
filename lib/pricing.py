import logging
import os
import boto3


logger = logging.getLogger(__name__)
PRICELIST_API_REGION = os.environ.get('PRICELIST_API_REGION', 'us-east-1')


def get_union_regions(suffix='\n'):
    """
    get location attribute values, convert sorted list
    """
    return [r + suffix for r in sorted(_get_union_regions())]


def _get_union_regions():
    """
    get location attribute values on several services
    """
    return set().union(
        _get_regions('AmazonEC2'),
        _get_regions('AmazonRDS'),
        _get_regions('AmazonS3'),
    )


def _get_regions(service_code):
    """
    get location attribute values from PricelistApi
    service_code: str
    """
    logger.info('start pricelist call service:{}'.format(service_code))
    client = boto3.client('pricing', region_name=PRICELIST_API_REGION)
    response = client.get_attribute_values(
        ServiceCode=service_code,
        AttributeName='location',
    )
    logger.info('end pricelist call service:{}'.format(service_code))
    if 'AttributeValues' not in response:
        return {}

    return {r['Value'] for r in response['AttributeValues']}
