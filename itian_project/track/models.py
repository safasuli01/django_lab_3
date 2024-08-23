from django.db import models

class Track(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return self.name
