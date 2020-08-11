from django.db import models

from django.contrib.auth.models import ( AbstractBaseUser, BaseUserManager)

class MyAccountManager(BaseUserManager):

    def create_user(self, username, email, password=None):

        if not email:
            return ValueError("Please enter you email")
        if not username:
            return ValueError("Please enter your username")
      
        user = self.model(
                          email=self.normalize_email(email),
                          username=username
                        )
        user.set_password(password)
        user.save(using=self.db) # Adding data to the database
        return user
    def create_superuser(self, username, email, password):
        if not email:
            return ValueError("Please enter you email")
        if not username:
            return ValueError("Please enter your username")
       
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=256)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    name = models.CharField(max_length=256)


    # That's the default variables which we have to create
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # What will be main parameter for sign in beside password (In our case it's username and password)
    USERNAME_FIELD = 'username'
    # What others fields user has to enter
    REQUIRED_FIELDS = ['email', ]

    objects = MyAccountManager()

    # Return username name
    def get_username(self):
        return self.username



    def has_perm(self, perm, obj=None):
        return True


    def has_module_perms(self, app_label):
        return self.is_admin






