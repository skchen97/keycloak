from django.contrib.auth import get_user_model
from django.db import models
from allauth.account.signals import user_logged_in


def user_logged_in_receiver(request, user):
    print(request)
    print(user)
