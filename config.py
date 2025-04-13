import environ
import json

env = environ.Env()
environ.Env.read_env('.env')


class Config:
    SECRET_KEY = env('SECRET_KEY')
    DEBUG = env('DEBUG') == 'True'
    
    REDIS_PASSWORD = env('REDIS_PASSWORD')
    REDIS_HOST = env('REDIS_HOST')
    REDIS_PORT = int(env('REDIS_PORT'))
    
    ACCESS_TOKEN_LIFETIME = int(env('ACCESS_TOKEN_LIFETIME'))
    REFRESH_TOKEN_LIFETIME = int(env('REFRESH_TOKEN_LIFETIME'))
    
    EMAIL_SENDER = env('EMAIL_SENDER')
    EMAIL_HOST = env('EMAIL_HOST')
    EMAIL_HOST_DOMAIN = env('EMAIL_HOST_DOMAIN')
    EMAIL_PORT = int(env('EMAIL_PORT'))
    EMAIL_HOST_USER = env('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

    POSTGRES_USER = env('POSTGRES_USER')
    POSTGRES_PASSWORD = env('POSTGRES_PASSWORD')
    POSTGRES_DB = env('POSTGRES_DB')
    POSTGRES_PORT = int(env('POSTGRES_PORT'))
    POSTGRES_HOST = env('POSTGRES_HOST')

    ALLOWED_HOSTS = json.loads(env('ALLOWED_HOSTS'))


config = Config()