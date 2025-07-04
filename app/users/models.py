from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager, BaseUserManager)
from django.db import models

class UserManager(BaseUserManager):
    # 일반 유저 함수 생성
    def create_user(self, email, password):
        if not email:
            raise ValueError('Please Enter an email Address')

        user = self.model(email=email)
        user.set_password(password)
        user.save()

        return user

    # 슈퍼 유저 함수 생성
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True

        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    # - email
    email = models.CharField(max_length=255, unique=True)

    # - password => custom_user 에 포함 되어 있어서 건드릴 필요 없다.

    # - nickname
    nickname = models.CharField(max_length=15)

    # - is_business
    is_business = models.BooleanField(default=False)

    # Permissions Mixin : 유저 권한 관리
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return f'email{self.email}, nickname{self.nickname}'
