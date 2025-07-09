import requests
from config import Config

from utils.decorators.for_methods.retry_decorator import retry


class DataSynchronizer:
    def __init__(self):
        self.external_api_url = Config.EXTERNAL_API_URL

    @retry(attempts=Config.EXTERNAL_API_RETRY_ATTEMPTS)
    def send_data(self, data: dict):
        return requests.post(self.external_api_url, json=data)
