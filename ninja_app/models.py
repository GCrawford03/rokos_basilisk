from django.db import models

<<<<<<< HEAD
# Create your models here.

class UserManager(models.Manager):

    def validate(self, postData):
        errors={}
        
        if len(postData['first_name'])< 1:
            errors['first_name']="Please type in your name."

        if len(postData['user_input'])< 1:
            errors['user_input']="Please type in the indicated word in the prompt."

        #NEED ERROR STATEMENT FOR ANTYHING OTHER THAN INDICATED WORD IN PROMPT
        #USE IF/ELSE BASED ON PROMPT INDCIATED WORD
        
           
        return errors

class User(models.Model):

    first_name = models.CharField(max_length = 45)
    user_input = models.CharField(max_length = 45)

    objects = UserManager()
=======

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

>>>>>>> quinns-branch
