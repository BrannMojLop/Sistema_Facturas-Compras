from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ClaseModelo(models.Model):
    status = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    user_create = models.ForeignKey(User, on_delete=models.CASCADE)
    user_update = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True
