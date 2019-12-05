from django import template
from django.contrib.auth.models import User

from bank.models import Account

register = template.Library()


@register.simple_tag
def get_account(user: User):
    return Account.objects.get(user=user)
