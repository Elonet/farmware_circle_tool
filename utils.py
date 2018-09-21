# -*- coding: utf-8 -*-

import os
import requests


def send_celery_script(script):
    """
    Send celery script

    :param script: Script to send
    :type script: dict
    """
    headers = {
        'Authorization': 'bearer {}'.format(os.environ['FARMWARE_TOKEN']),
        'content-type': "application/json"
    }

    response = requests.post(os.environ['FARMWARE_URL'] + '/api/v1/celery_script', json=script, headers=headers)

    return response


def get_resource(uri):
    """
    Get resource from API

    :param uri: Uri of resource
    :type uri: str

    :return: Resource
    """
    headers = {
        'Authorization': 'bearer {}'.format(os.environ['FARMWARE_TOKEN']),
        'content-type': "application/json"
    }

    return requests.get(os.environ['FARMWARE_URL'] + uri, headers=headers)


def log(message, message_type):
    """
    Send a message to the log.

    :param message: Message
    :type message: str
    :param message_type: Message type
    :type message_type: str
    """

    try:
        os.environ['FARMWARE_URL']
    except KeyError:
        print(message)
    else:
        log_message = '[Circle tool] ' + str(message)
        send_celery_script({
            "kind": "send_message",
            "args": {
                "message": log_message,
                "message_type": message_type
            }
        })
