from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model where the email address is the unique identifier
    and has an is_admin field to allow access to the admin app 
    """
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The email must be set"))
        if not password:
            raise ValueError(_("The password must be set"))
        email = self.normalize_email(email)
        try:
            user_admin = self.request.user
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            if user_admin.is_superuser:
                extra_fields.setdefault('role', 1)
            else:
                extra_fields.setdefault('role', 3)
        except:
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            extra_fields.setdefault('role', 3)
            user.save()
        
        return user

    def create_admin_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 1)

        if extra_fields.get('role') != 1:
            raise ValueError('Admin must have role of Global Admin')
        return self.create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 2)

        if extra_fields.get('role') != 2:
            raise ValueError('Admin must have role of Global Admin')
        return self.create_user(email, password, **extra_fields)