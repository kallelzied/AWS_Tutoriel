import json
import logging
import os
import time

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def lambda_handler(event, context):
    logger.info("Read user_id and date from sns")
    message = _parse_event(event)
    logger.info(message)


def _parse_event(event):
    message = event['Records'][0]['Sns']['Message']
    message = json.loads(message)
    return {'user_id': int(message['user_id']),
            'date': int(message['date'])}
