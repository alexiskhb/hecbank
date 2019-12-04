from .models import Payment, Account
from django.contrib.auth.models import User
from sys import stderr


def make_transaction(sender: str, receiver: str, amount: int):
    if amount <= 0:
        return False

    try:
        sender = User.objects.get_by_natural_key(sender)
        sender_account: Account = Account.objects.get(user=sender)
    except Exception as e:
        print(e, file=stderr)
        return False

    if sender_account.amount < amount:
        return False
    try:
        receiver = User.objects.get_by_natural_key(receiver)
        receiver_account: Account = Account.objects.get(user=receiver)
    except Exception as e:
        print(e, file=stderr)
        return False

    sender_account.amount -= amount
    receiver_account.amount += amount
    payment = Payment(sender=sender, receiver=receiver, amount=amount)

    # TODO: this code is completely NOT SAVE
    payment.save()
    sender_account.save()
    receiver_account.save()
    return True
