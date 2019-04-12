from django.db import models


# Create your models here.
class UsersData(models.Model):

    id = models.AutoField(primary_key=True, null=False, unique=True)
    username = models.CharField(max_length=16, blank=False, unique=True)
    password = models.CharField(max_length=16, blank=False)
    user_token = models.CharField(max_length=100, null=True)

    class first:
        db_table = "user"


class RunScriptsData(models.Model):

    id = models.AutoField(primary_key=True, null=False, unique=True)
    username = models.CharField(max_length=16)
    result = models.CharField(max_length=10)
    log = models.CharField(max_length=200)
    time = models.DateTimeField()

    class second:
        db_table = "run_scripts_data"
