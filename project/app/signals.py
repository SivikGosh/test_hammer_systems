# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import InviteCode, User


@receiver(post_save, sender=User)
def create_invite_code(sender, instance, created, **kwargs):
    if created:
        InviteCode.objects.create(user=instance)
