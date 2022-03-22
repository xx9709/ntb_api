from django.db import models
from django.contrib.auth.models import AbstractUser



   
# for users and their roll
class User(AbstractUser):
    name = models.CharField(max_length=70,null=False, blank=False)
    email = models.EmailField(max_length=255, unique=True)
    roll = models.CharField(max_length=50,null = False, blank=False)   
    sum = models.IntegerField(null=True, blank=True)
    dollor = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=255, null=False, blank=False)

    USERNAMEE_FIELD = 'name'
    REQUIRED_FILELDS = []
    
#to enter a list of materials for the engineer
class Material(models.Model):
    name = models.CharField(max_length=70, null = False, blank=False)

#history of transactions of money and materials
class Transaction(models.Model):
    owner = models.ForeignKey(User, related_name='owner', null=True, blank=True, on_delete=models.SET_NULL)
    getter = models.ForeignKey(User, related_name='getter', null=True, blank=True, on_delete=models.SET_NULL)
    transaction = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    