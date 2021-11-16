from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser, Group
from django.db import models, transaction
from django.utils import timezone


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, username, full_name, password, **extra_fields):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        try:
            with transaction.atomic():
                user = self.model(email=email, username=username, full_name=full_name, **extra_fields)
                group = Group.objects.get(extra_fields["group_id"])
                group.user_set.add(user)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_superuser(self, email, username, full_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, username, full_name, password, **extra_fields)

    def create_user(self, email, username, full_name,password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, username, full_name, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=200, unique=True)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateTimeField(default=timezone.now, editable=False)
    about = models.TextField(_('about_salom'), max_length=500, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']

    def __str__(self):
        return self.email