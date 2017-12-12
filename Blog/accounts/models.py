from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)

class Feedback1(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=150,default='')

# class Bio(models.Model):
#         user = models.ForeignKey(User,on_delete=models.CASCADE)
#         description = models.CharField(max_length = 150,default ='')
#         phone = models.IntegerField(default=0)
