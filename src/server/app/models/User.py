from django.db.models import CharField, AutoField, ForeignKey, SET_NULL
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django_paranoid.models import ParanoidModel, ParanoidModelManager


class UserManager(ParanoidModelManager, BaseUserManager):
    pass


class User(AbstractBaseUser, PermissionsMixin, ParanoidModel):
    id = AutoField(primary_key=True)
    login_id = CharField(unique=True, max_length=255)
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    en_first_name = CharField(max_length=150)
    en_last_name = CharField(max_length=150)
    division = ForeignKey("Division", blank=True, null=True, on_delete=SET_NULL)
    role = ForeignKey("Role", blank=True, null=True, on_delete=SET_NULL)

    USERNAME_FIELD = "login_id"

    objects = UserManager()
