from django.db import models
from account.models import *
from track.models import *
from django.urls import reverse
import os
from django.conf import settings


# Create your models here.
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.DateField()
    photo = models.ImageField(upload_to="trainee/images/", blank=True, null=True)
    account_obj = models.ForeignKey(
        "account.Account", on_delete=models.CASCADE, null=True
    )
    track_obj = models.ForeignKey("track.Track", on_delete=models.CASCADE, null=True)

    @staticmethod
    def get_url():
        return reverse("trainee_list")

    def getphoto(self):
        return f"/media/{self.photo}"

    @classmethod
    def list_trainee(cls):
        return cls.objects.all()

    @classmethod
    def create_trainee(
        cls,
        first_name,
        last_name,
        age,
        photo,
        account_obj,
        track_obj,
    ):
        traineeobj = cls(
            first_name=first_name,
            last_name=last_name,
            age=age,
            photo=photo,
            account_obj=account_obj,
            track_obj=track_obj,
        )
        traineeobj.save()
        return cls.get_url()

    @classmethod
    def update_trainee(
        cls,
        id,
        first_name,
        last_name,
        age,
        photo,
        account_obj,
        track_obj,
    ):
        traineeobj = cls.objects.get(pk=id)
        traineeobj.first_name = first_name
        traineeobj.last_name = last_name
        traineeobj.age = age

        if photo and traineeobj.photo and traineeobj.photo != photo:
            old_photo_path = os.path.join(settings.MEDIA_ROOT, traineeobj.photo.name)
            if os.path.exists(old_photo_path):
                os.remove(old_photo_path)

        traineeobj.photo = photo
        traineeobj.account_obj = account_obj
        traineeobj.track_obj = track_obj
        traineeobj.save()
        return cls.get_url()

    @classmethod
    def delete_trainee(cls, id):
        traineeobj = cls.objects.get(pk=id)
        if traineeobj.image:
            photo_path = os.path.join(settings.MEDIA_ROOT, traineeobj.photo.name)
            print(f"Attempting to delete image: {photo_path}")
            if os.path.exists(photo_path):
                os.remove(photo_path)
                print("Photo has beeb deleted successfully")
            else:
                print("Image  does not exist")

        traineeobj.delete()
        return cls.get_url()

    @classmethod
    def details_trainee(cls, id):
        return cls.objects.get(pk=id)