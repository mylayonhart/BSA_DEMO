from django.contrib import admin
from .models import Territory, Account, Prescriber, Prescription

admin.site.register(Territory)
admin.site.register(Account)
admin.site.register(Prescriber)
admin.site.register(Prescription)
