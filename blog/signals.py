# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post
from .utils import send_email_to_subscribers

@receiver(post_save, sender=Post)
def post_created(sender, instance, created, **kwargs):
    if created:
        send_email_to_subscribers(instance)
        
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
# 
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()