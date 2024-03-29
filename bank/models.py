from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    can_send = models.BooleanField(default=True)
    can_receive = models.BooleanField(default=True)


class Payment(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='PaymentReceiver')
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
