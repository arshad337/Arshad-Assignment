import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    print(f"Signal handler thread ID: {threading.get_ident()}")

def create_user():
    print(f"Caller thread ID: {threading.get_ident()}")
    user = User.objects.create(username='testuser')

create_user()
