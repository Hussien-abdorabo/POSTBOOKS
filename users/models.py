from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField( User , on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to='profiles'
                              ,validators=[FileExtensionValidator(["png","jpg","webp"])])

    def __str__(self) :
        return f"{self.user.username}"