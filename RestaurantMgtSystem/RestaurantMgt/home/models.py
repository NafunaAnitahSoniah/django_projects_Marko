from django.db import models

# Create your models here.
class UserAccount(models.Model):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    name = models.TextField()
    position = models.TextField(blank=True)
    password = models.TextField()
    role = models.CharField(max_length=25, default='Customer') # Admin, Finance or Customer
    date_joined = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20) # Active or Inactive

class Food(models.Model):
    title = models.TextField()
    description = models.TextField()
    image = models.TextField(blank=True)
    calories = models.IntegerField()
    is_vegetarian = models.BooleanField(default=False)
    date_add = models.DateField(auto_now_add=True)
    price = models.IntegerField() # 20,000

class Table(models.Model):
    table_name = models.TextField()
    is_vip = models.BooleanField(default=False)  

class Transaction(models.Model):
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    userAccount = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    quantity = models.IntegerField(default=1)
    method_of_payment = models.TextField(default="Cash") # Cash, Mobile Money, Bank Card, Crypto, Loyalty Points
    date = models.DateTimeField(auto_now_add=True)