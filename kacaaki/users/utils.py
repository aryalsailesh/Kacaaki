import datetime

import pytz
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator


def custom_create_token(token_model, user, serializer):
    token = token_model.objects.create(user=user)
    utc_now = timezone.now()
    utc_now = utc_now.replace(tzinfo=pytz.utc)
    token.created = utc_now
    token.save()
    return token



def user_verification_email(user):
    token = generate_token(user)
    send_mail(
        "Verify your email",
        "Please verify your email by clicking the link below: "
        f"http://127.0.0.1:8000/api/user/verify-email/{token}",
        "noreply@gmail.com",
        [user.email],
        fail_silently=False,
    )


def generate_token(user):
    token = PasswordResetTokenGenerator()
    return token.make_token(user)

def verify_token(token):
    token_generator = PasswordResetTokenGenerator()
    users = get_user_model().objects.filter(is_active=False)
    for user in users:
        if token_generator.check_token(user, token):
            return user
    return None