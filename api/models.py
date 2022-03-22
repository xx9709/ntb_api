from django.db import models
from django.contrib.auth.models import AbstractUser



   
# for users and their roll
class User(AbstractUser):
    name = models.CharField(max_length=255,null=False, blank=False, unique=False)
    email = models.EmailField(max_length=255, null = True, blank = True,unique=True)
    roll = models.CharField(max_length=255,null = False, blank=False)   
    sum = models.IntegerField(null=True, blank=True)
    dollor = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=255, null=False, blank=False)

    USERNAMEE_FIELD = 'username'
    REQUIRED_FILELDS = []
    
#to enter a list of materials for the engineer
class Material(models.Model):
    name = models.CharField(max_length=70, null = False, blank=False)

# history of transactions of money and materials
class Transaction(models.Model):
    owner = models.ForeignKey(User, related_name='owner', null=True, blank=True, on_delete=models.SET_NULL)
    getter = models.ForeignKey(User, related_name='getter', null=True, blank=True, on_delete=models.SET_NULL)
    paymethod = models.BooleanField(blank=True, null=True) #if True paymethod in UZS {so'm} else: USD & $
    pay = models.IntegerField(blank=True, null=True) #if True paymethod in UZS {so'm} else: USD & $
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    