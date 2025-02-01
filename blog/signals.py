# signals.py
from django.db.models.signals import post_save
from .models import Post
from django.dispatch import receiver
from .utils import send_email_to_subscribers
from django.contrib.auth.models import User

@receiver(post_save, sender=Post)
def post_created(sender, instance, created, **kwargs):
    if created:
        send_email_to_subscribers(instance)
        