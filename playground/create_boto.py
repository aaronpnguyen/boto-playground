import boto3
import logging
from botocore.exceptions import ClientError

def create_bucket(bucket_name):
    try:
        client = boto3.client('s3')
        client.create_bucket(Bucket = bucket_name) # Region is defaulted to 'us-east-1', to change add region_name = <REGION> as param
    except ClientError as error:
        logging.error(error)
        return False
    return True