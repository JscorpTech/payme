import base64
from decimal import Decimal

from django.conf import settings

assert settings.PAYCOM_SETTINGS.get('KASSA_ID') is not None
assert settings.PAYCOM_SETTINGS.get('ACCOUNTS') is not None
assert settings.PAYCOM_SETTINGS['ACCOUNTS'].get('KEY') is not None

TOKEN = settings.PAYCOM_SETTINGS['TOKEN']
KEY = settings.PAYCOM_SETTINGS['ACCOUNTS']['KEY']


class PayComResponse(object):
    LINK = 'https://checkout.paycom.uz'

    def create_initialization(self, amount: Decimal, order_id: str, return_url: str) -> str:
        """

        documentation : https://help.paycom.uz/ru/initsializatsiya-platezhey/otpravka-cheka-po-metodu-get

        >>> self.create_initialization(amount=Decimal(5000.00), order_id='1', return_url='https://example.com/success/')
        """

        params = f"m={TOKEN};ac.{KEY}={order_id};a={amount};c={return_url}"
        encode_params = base64.b64encode(params.encode("utf-8"))
        encode_params = str(encode_params, 'utf-8')
        url = f"{self.LINK}/{encode_params}"
        return url
