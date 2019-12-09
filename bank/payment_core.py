from .models import Payment, Account
from django.contrib.auth.models import User
from sys import stderr
from django.db import transaction
from .settings import DEBUG


def make_transaction(sender: str, receiver: str, amount: int):
    if amount <= 0 or sender == receiver:
        return False

    try:
        sender = User.objects.get_by_natural_key(sender)
        sender_account: Account = Account.objects.get(user=sender)
    except Exception as e:
        if DEBUG:
            print(e, file=stderr)
        return False

    if sender_account.amount < amount or not sender_account.can_send:
        return False

    try:
        receiver = User.objects.get_by_natural_key(receiver)
        receiver_account: Account = Account.objects.get(user=receiver)
    except Exception as e:
        if DEBUG:
            print(e, file=stderr)
        return False

    if not receiver_account.can_receive:
        return False

    sender_account.amount -= amount
    receiver_account.amount += amount
    payment = Payment(sender=sender, receiver=receiver, amount=amount)

    try:
        with transaction.atomic():
            payment.save()
            sender_account.save()
            receiver_account.save()
    except Exception as e:
        if DEBUG:
            print(e, file=stderr)
        return False

    return True
