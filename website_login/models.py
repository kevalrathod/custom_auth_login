from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



MEAL_TYPE=(
    ('BODYBUILDING','bodybuilding'),
    ('WEIGHTLOSE','weightlose'),
    ('LEANBODY','leanbody'),
    ('SHREDED','shreded'),
    ('BULKBODY','bulkbody'),
)

DIET_PLAN=(
    ('NONVEG','nonveg'),
    ('VEG','veg'),
)


class Profile(models.Model):
    
    user_name= models.CharField(max_length=40)
    upassword = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    height = models.IntegerField(null=True,blank=True)
    weight = models.IntegerField(null=True,blank=True)
    body_type = models.CharField(
        choices=MEAL_TYPE,
        blank=True,
        max_length=40)
    diet_type = models.CharField(
        choices=DIET_PLAN,
        blank=True,
        max_length=40)
    














    
