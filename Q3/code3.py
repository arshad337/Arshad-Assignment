from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    print(f"Signal: Created a profile for {instance.username}")
    # Simulating related profile creation
    instance.profile = "UserProfile"

def create_user():
    try:
        with transaction.atomic():
            print("Creating user inside transaction...")
            user = User.objects.create(username='testuser')
            raise Exception("Simulated error")
    except Exception as e:
        print(f"Error: {e}")

    # Check if user was created after rollback
    if User.objects.filter(username='testuser').exists():
        print("User still exists")
    else:
        print("User creation was rolled back")

create_user()
