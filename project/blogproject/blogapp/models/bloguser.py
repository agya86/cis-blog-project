from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')


# login user

#user profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile=models.CharField(validators=[phone_regex], max_length=17, blank=True)
    address=models.CharField(max_length=200 ,blank=True)
    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()