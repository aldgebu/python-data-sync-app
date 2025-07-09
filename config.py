import os

from datetime import timedelta
from dotenv import load_dotenv

from models.general.env_type_enum import EnvTypeEnum


load_dotenv()


def get_database_uri(env_type: EnvTypeEnum):
    db_uri = f'postgresql://' \
            f'{os.environ.get('DATABASE_USER')}' \
            f':{os.environ.get('DATABASE_USER_PASSWORD')}' \
            f'@{os.environ.get('DATABASE_HOST')}' \
            f':{os.environ.get('DATABASE_PORT_LOCAL')}' \
            f'/{os.environ.get(f'{env_type.value}_DATABASE_NAME')}'
    return db_uri


class Config:
    DEBUG = False

    APP_HOST = os.environ['APP_HOST']
    APP_PORT_DOCKER = os.environ['APP_PORT_DOCKER']
    ENV_TYPE = EnvTypeEnum(os.environ.get('ENV_TYPE', EnvTypeEnum.DEVELOPMENT.value))

    # JWT related
    JWT_REFRESH_TOKEN_EXPIRES = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_LIFETIME = timedelta(hours=1)
    JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']

    EXTERNAL_API_URL = os.environ['EXTERNAL_API_URL']
    SYNC_INTERVAL_MINUTES = os.environ.get('SYNC_INTERVAL_MINUTES', 10)
    EXTERNAL_API_RETRY_ATTEMPTS = os.environ.get('EXTERNAL_API_RETRY_ATTEMPTS', 5)


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = get_database_uri(EnvTypeEnum.PRODUCTION)


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = get_database_uri(EnvTypeEnum.DEVELOPMENT)


class ConfigManager:
    config_mapping = {
        EnvTypeEnum.PRODUCTION: ProductionConfig,
        EnvTypeEnum.DEVELOPMENT: DevelopmentConfig,
    }

    @classmethod
    def get_config(cls):
        return ConfigManager.config_mapping.get(Config.ENV_TYPE)
