from django.db import models

# Create your models here.
class Guest(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)
    id_number = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name

    # To get all users in the table
    @classmethod
    def get_all_users(cls):
        return cls.objects.all()

    @classmethod
    def get_oneUser(cls,id):
        guest = cls.objects.get(id=id)
        return guest
