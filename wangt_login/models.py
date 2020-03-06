from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)
    gender = models.BooleanField()
    creat_time = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=255)
    head_img = models.CharField(max_length=255)
    brief = models.CharField(max_length=255)

    class Meta:
        db_table = "t_user"