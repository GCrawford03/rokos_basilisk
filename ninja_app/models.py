from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class PlayerManager(models.Manager):
    def reg_val(self, postData):
        errors = {}
        check = Player.objects.filter(email=postData['email'])
        if len(postData['username']) < 2:
            errors['username'] = ("Username must be at least 2 Characters") 
        if not EMAIL_REGEX.match(postData['email']):
            errors['reg_email'] = ("Invalid email address!")
        elif check:
            errors['reg_email'] = "Email address is already registered!"
        if len(postData['password']) <8:
            errors['password'] = 'Password must be at least 8 characters!'
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = 'Password must match!'
        return errors
    def login_val(self,postData):
        errors = {}
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ("Invalid email address!")
        return errors   

class Player(models.Model):
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = PlayerManager()  

