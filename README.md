[![Downloads](https://img.shields.io/pypi/v/JscorpTechPayme)](https://pypi.org/project/JscorpTechPayme)

### Requirements

````
pip install django
pip install djangorestframework
pip install JscorpTechPayme
pip install requests

# supported versions
python 3.5 +
django 2 +
djangorestframework 3.7 +
PaycomUz 2 +
````

**settings.py**

```python
PAYCOM_SETTINGS = {
    "KASSA_ID": "KASSA ID",  # token
    "SECRET_KEY": "TEST KEY OR PRODUCTIN KEY",  # password
    "ACCOUNTS": {
        "KEY": "order_id"
    }
}

INSTALLED_APPS = [
    'rest_framework',
    'paycomuz',
    ...
]
```

```
python manage.py migrate
```

### Create paycom user

```python
python
manage.py
create_paycom_user
```

### view.py

```python
from paycomuz.views import MerchantAPIView
from paycomuz.methods_subscribe_api import Paycom
from django.urls import path


class CheckOrder(Paycom):
    def check_order(self, amount, account):
        return self.ORDER_FOUND


class TestView(MerchantAPIView):
    VALIDATE_CLASS = CheckOrder


urlpatterns = [
    path('paycom/', TestView.as_view())
]
```

### create_initialization.py

https://help.paycom.uz/uz/initsializatsiya-platezhey/otpravka-cheka-po-metodu-get

```python
from paycomuz.methods_subscribe_api import Paycom

paycom = Paycom()
url = paycom.create_initialization(amount=5.00, order_id='197', return_url='https://example.com/success/')
print(url)
```
