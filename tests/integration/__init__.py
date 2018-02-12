from os import environ

__author__ = 'aleks'


def ensure_aws_creds():
    try:
        environ['AWS_ACCESS_KEY_ID']
    except KeyError:
        print('Environment variable AWS_ACCESS_KEY_ID is not defined.')
        environ['AWS_ACCESS_KEY_ID'] = raw_input('Please enter it: ')
    try:
        environ['AWS_SECRET_ACCESS_KEY']
    except KeyError:
        print('Environment variable AWS_SECRET_ACCESS_KEY is not defined.')
        environ['AWS_SECRET_ACCESS_KEY'] = raw_input('Please enter it: ')
