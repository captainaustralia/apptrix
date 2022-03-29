from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from core.funcs import get_file_path


class UserManager(BaseUserManager):
    """
    BASE USER MANAGER FOR PARTICIPANT
    """
    def create_user(self, email, password, name, last_name, gender, is_staff, is_admin=False,
                    is_active=True,
                    **kwargs):
        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.email = email
        user_obj.name = name
        user_obj.last_name = last_name
        user_obj.gender = gender
        user_obj.is_staff = is_staff
        user_obj.is_admin = is_admin
        user_obj.is_active = is_active
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email, password):
        user = self.create_user(
            name=None,
            last_name=None,
            gender=None,
            email=email,
            password=password,
            is_staff=True,
            is_admin=True,
            is_active=True,
        )
        return user


class Participant(AbstractBaseUser, PermissionsMixin):
    """
    BASE USER MODEL
    """
    gender_types = [
        ('male', 'male'),
        ('female', 'female')
    ]

    name = models.CharField(
        max_length=100,
        blank=False,
        null=True
    )

    last_name = models.CharField(
        max_length=100,
        blank=False,
        null=True
    )

    gender = models.CharField(
        choices=gender_types,
        max_length=6,
        blank=False,
        null=True
    )

    email = models.EmailField(
        unique=True,
        blank=False,
        null=True
    )

    avatar = models.ImageField(
        upload_to=get_file_path
    )

    is_active = models.BooleanField(default=False)

    is_admin = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f'Name:{self.name} , Last name : {self.last_name}'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    # ADD PERMISSIONS FOR ADMIN PANEL

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
