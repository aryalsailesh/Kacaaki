from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class NepaliStudentManager(BaseUserManager):
 
    def create_nepali_student(self,email, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        student = self.create_student(
                          email=self.normalize_email(email),
                        )
        student.set_password(password)
        student.save()
        return student


class DanceStudentManager(BaseUserManager):
 
    def create_dance_student(self,email, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        student = self.create_student(
                          email=self.normalize_email(email),
                        )
        student.set_password(password)
        student.save()
        return student