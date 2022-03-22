from django.db import models

# for users and their roll
class User(models.Model):
    name = models.CharField(max_length=70,null=False, blank=False)
    roll = models.CharField(max_length=50,null = False, blank=False)

#for for the current state of the user 
class Bill(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    sum = models.IntegerField(null=True, blank=True)
    dollor = models.IntegerField(null=True, blank=True)

#to enter a list of materials for the engineer
class Material(models.Model):
    name = models.CharField(max_length=70, null = False, blank=False)

#history of transactions of money and materials
class Transaction(models.Model):
    from_user = models.ForeignKey(User, related_name='transmitter', null=True, blank=True, on_delete=models.SET_NULL)
    to_user = models.ForeignKey(User, related_name='recipient', null=True, blank=True, on_delete=models.SET_NULL)
    transaction = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    