from django.contrib.auth.models import User
from django.db import models

from modules.exceptions.model_exceptions import UserAlreadyExist


def create_normal_user(username: str, email: str, password: str) -> models.Model:
    if is_exist_username(username):
        raise UserAlreadyExist(username)
    if is_exist_user_email(email):
        raise UserAlreadyExist(email)

    user = User.objects.create_user(username, email, password)
    return user


def is_exist_username(username: str) -> bool:
    try:
        User.objects.get(username = username)

    except User.DoesNotExist:
        return False

    return True


def is_exist_user_email(email: str) -> bool:
    try:
        User.objects.get(email = email)

    except User.DoesNotExist:
        return False

    return True
