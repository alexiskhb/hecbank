from django.contrib import admin

from .models import Payment
from .models import Account

admin.site.register(Payment)
admin.site.register(Account)
