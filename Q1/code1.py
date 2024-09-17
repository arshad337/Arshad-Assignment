import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Simulated email sending function
def send_welcome_email(user):
    print(f"Sending welcome email to {user.username}...")
    time.sleep(3)  # Simulate the time it takes to send an email (3 seconds)
    print("Welcome email sent.")

# Signal receiver that triggers after a User is saved
@receiver(post_save, sender=User)
def user_saved(sender, instance, created, **kwargs):
    if created:
        print("User created, sending welcome email...")
        send_welcome_email(instance)

# Function that creates a new user
def create_user():
    print("Registering new user...")
    user = User.objects.create(username='newuser', email='newuser@example.com')
    print("User registration complete.")

# Call the function to create a user
create_user()
