import os
import django
import random
from string import digits, ascii_letters
from django.db.utils import IntegrityError
from django.db import transaction

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bank.settings")
django.setup()

from django.contrib.auth.models import User
from bank.models import Account


INIT_AMOUNT = 250
NICE_LETTERS = tuple(set(digits + ascii_letters) - {'O', '0', 'l', 'I', '1'})


def random_username(length=6, alphabet=digits):
    return ''.join(random.choices(alphabet, k=length))


def random_pswd(length=7, alphabet=NICE_LETTERS):
    return ''.join(random.choices(alphabet, k=length))


def add_record(username, password, amount=0, can_send=True, can_receive=True, file=None):
    if file is None:
        file = open('users', 'a')
    file.write(f"{username} {password}\n")
    try:
        with transaction.atomic():
            user = User.objects.create_user(username=username, password=password)
            account = Account(user=user, amount=amount, can_send=can_send, can_receive=can_receive)
            account.save()
    except IntegrityError:
        return False
    return True


def add_store(file=None):
    return add_record(random_username(length=3, alphabet=digits),
                      random_pswd(), amount=0, can_send=False, can_receive=True, file=file)


def add_user(user_prefix='', file=None):
    return add_record(user_prefix + random_username(length=6 - len(user_prefix)),
                      random_pswd(), amount=INIT_AMOUNT, file=file)


with open('users.txt', 'w') as f:
    for i in range(50):
        add_store(file=f)
    for i in range(500):
        add_user(file=f)
