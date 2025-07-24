from django.contrib import admin
from home.models import UserAccount, Food, Table, Transaction

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(Food)
admin.site.register(Table)
admin.site.register(Transaction)
