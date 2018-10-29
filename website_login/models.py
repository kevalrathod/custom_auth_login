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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.IntegerField(blank=True)
    weight = models.IntegerField(blank=True)
    body_type = models.CharField(
        choices=MEAL_TYPE,
        blank=True,
        max_length=40)
    diet_type = models.CharField(
        choices=DIET_PLAN,
        blank=True,
        max_length=40)

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()