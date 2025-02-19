import environ

env = environ.Env()
environ.Env.read_env('.env')


class Config:
    SECRET_KEY = env('SECRET_KEY')
    DEBUG = env('DEBUG')
    
    REDIS_PASSWORD = env('REDIS_PASSWORD')
    REDIS_HOST = env('REDIS_HOST')
    REDIS_PORT = int(env('REDIS_PORT'))
    
    ACCESS_TOKEN_LIFETIME = int(env('ACCESS_TOKEN_LIFETIME'))
    REFRESH_TOKEN_LIFETIME = int(env('REFRESH_TOKEN_LIFETIME'))
    
    EMAIL_SENDER = env('EMAIL_SENDER')

    POSTGRES_USER = env('POSTGRES_USER')
    POSTGRES_PASSWORD = env('POSTGRES_PASSWORD')
    POSTGRES_DB = env('POSTGRES_DB')
    POSTGRES_PORT = int(env('POSTGRES_PORT'))
    POSTGRES_HOST = env('POSTGRES_HOST')


config = Config()