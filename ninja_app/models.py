from django.db import models


class PlayerManager(models.Manager):
    def reg_val(self, postData):
        errors = {}
        if len(postData['username']) < 2:
            errors['username'] = ("Username must be at least 2 Characters") 
        if len(postData['password']) <8:
            errors['password'] = 'Password must be at least 8 characters!'
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = 'Password must match!'
        return errors

class Player(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = PlayerManager()  

