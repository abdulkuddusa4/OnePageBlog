from django.db import models
from django.contrib.auth.models import User


class EmailValidator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_validate = models.BooleanField(default=False)
