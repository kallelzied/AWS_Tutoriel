import json
import logging
import os
import time
import boto3

sns = boto3.client('sns')
USER_LAST_LOGIN_SNS_TOPIC_ARN = os.getenv('USER_LAST_LOGIN_SNS_TOPIC_ARN')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def lambda_handler(event, context):
    logger.info("Recording last login date")
    user_id = event['user_id']
    record_last_login_date(user_id)


def record_last_login_date(user_id):
    sns_message = {
        'userId': int(user_id),
        'date': int(time.time())
    }
    publish_to_sns(USER_LAST_LOGIN_SNS_TOPIC_ARN, sns_message)


def publish_to_sns(topic_arn, message):
    message= json.dumps(message)
    logger.info("Message: {}".format(message))
    response = sns.publish(TopicArn=topic_arn, Message=message)
    log_msg = "Message published to SNS:\nMessage: {}\nResponse:\n{}".format(message, str(response))
    logger.info(log_msg)
