import urllib
import boto3

s3 = boto3.client('s3')


def lambda_handler(event, context):

    # Get the object from the event and show its content type
    bucket = event['bucket']
    key = urllib.unquote_plus(event['key'].encode('utf8'))
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e