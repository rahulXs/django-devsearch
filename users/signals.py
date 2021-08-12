from django.db.models.signals import post_save, post_delete
# for implementing signals via decorator
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

# triggers creation of profile when user is created

# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

# Delete user when profile is deleted

def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)

# Note: Also, update apps.py file because signals.py is separate file.