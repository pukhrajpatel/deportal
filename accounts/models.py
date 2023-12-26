from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.



# Create your models here.
## Custom UserAccountManager Model
class UserAccountManager(BaseUserManager):
    def create_user(self,email,name=None,password=None,**extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        
        email = self.normalize_email(email)
        name = name
        user = self.model(email=email,name=name,**extra_fields)
        user.set_password(password)
        
        user.save()
        
        return user
    
    def create_superuser(self,email,name,password,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        
        
        return self.create_user(email=email,name=name,password=password,**extra_fields)
        

## User Account Model
class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def __str__(self):
        return self.email