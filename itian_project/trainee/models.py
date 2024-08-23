from django.db import models
from account.models import *
from track.models import *


# Create your models here.
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    account_obj = models.ForeignKey(Account, on_delete=models.CASCADE)
    track_obj = models.ForeignKey(Track, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
