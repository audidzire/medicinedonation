# accounts.models.py

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# accounts.models.py

class UserManager(BaseUserManager):
    def create_user(self, email, full_name, city, mobile_number, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')

        if not full_name:
            raise ValueError('Users must have a fullname')
        if not city:
            raise ValueError('Users must have a city')
        if not mobile_number:
            raise ValueError('Users must have a mobile_number')



        user = self.model(
            email=self.normalize_email(email),
            full_name = full_name,
            city = city,
            mobile_number = mobile_number,
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email,full_name, city, mobile_number, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            full_name = full_name,
            city = city,
            mobile_number = mobile_number,
            
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email,full_name, city, mobile_number, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            full_name = full_name,
            city = city,
            mobile_number = mobile_number,
            
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    full_name = models.CharField(max_length=100, blank=True, null=True)
    city= models.CharField(max_length=100, blank=True, null=True)
    mobile_number = models.CharField( max_length=10,blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    objects = UserManager()

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name','city','mobile_number'] # Email & Password are required by default.
    
    
    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active