from django.db import models


# Create your models here.
class User(models.Model):
    class Meta:
        db_table = 'LoginTable'

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
