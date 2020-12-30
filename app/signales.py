from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Account


@receiver(post_save, sender=get_user_model())
def create_account(sender, instantce, created, **kwags):
    if created:
        Account.objects.create(user=instantce)
