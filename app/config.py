import os

class Config(object):
    SECRET_KEY = os.environ.get('MICROBLOG_SECRET_KEY') or 'you-will-never-guess'
