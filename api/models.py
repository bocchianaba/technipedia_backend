from django.db import models
import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from pytz import country_names

from .managers import CustomUserManager

country_choices=((value, value) for key,value in country_names.items())

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    # These fields tie to the roles!
    ADMIN = 1
    MANAGER = 2
    VISITOR = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (VISITOR, 'Visitor'),
    )
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    email = models.EmailField(unique=True)
    username = models.CharField( max_length=30,default=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    profil_img=models.ImageField(upload_to='profil_img/%Y/%m/%d', blank=True)
    is_deleted = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    created_by = models.EmailField()
    modified_by = models.EmailField()
    country=models.CharField(max_length=50, blank=True,choices=country_choices)
    is_superuser = models.BooleanField(default=False)
    # products_liked=models.ManyToManyField('Product', related_name='likes', blank=True)
    # products_disliked=models.ManyToManyField('Product', related_name='dislikes', blank=True)
    # products_loved=models.ManyToManyField('Product', related_name='loves', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
