from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone, mobile, user_team, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")
        if not user_team:
            raise ValueError("Users must have a team selected")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            mobile=mobile,
            user_team=user_team,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user

    def verifyAccount(self, user, user_input, code):
        if user_input == code:
            user.is_active = True
            user.save(using=self._db)
            return user


class User(AbstractBaseUser):
    TEAM_CHOICES = (
        ("MANAGEMENT", "Gestion"),
        ("SALES", "Ventes"),
        ("SUPPORT", "Support"),
    )

    username = None
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    phone = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    user_team = models.CharField(
        max_length=20,
        choices=TEAM_CHOICES,
        blank=True,
        null=True,
        verbose_name="équipe",
    )

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
