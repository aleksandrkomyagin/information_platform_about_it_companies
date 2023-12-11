"""User manager model module."""
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name):
        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.password = password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.model(email=self.normalize_email(email))
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.password = password
        user.set_password(password)
        user.save(using=self._db)
        return user

    @classmethod
    def normalize_email(cls, email):
        """Normalize the email address by lowercase."""
        email = email or ""
        return email.lower()
