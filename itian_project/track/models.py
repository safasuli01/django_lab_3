from django.db import models
from django.urls import reverse
import os
from django.conf import settings


# Create your models here.
class Track(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to="track/photo/", blank=True, null=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_url():
        return reverse("track_list")

    def getimage(self):
        return f"/media/{self.photo}"

    @classmethod
    def getall(cls):
        return [
            (
                track.id,
                track.name,
                track.description,
                track.photo,
            )
            for track in cls.objects.all()
        ]

    @classmethod
    def list_track(cls):
        return cls.objects.all()

    @classmethod
    def create_track(cls, name, description, photo):
        trackobj = cls()
        trackobj.name = name
        trackobj.description = description
        trackobj.photo = photo
        trackobj.save()
        return cls.get_url()

    @classmethod
    def update_track(cls, id, name, description, photo):
        trackobj = cls.objects.get(pk=id)
        trackobj.name = name
        trackobj.description = description

        if photo and trackobj.photo and trackobj.photo != photo:
            old_photo = os.path.join(settings.MEDIA_ROOT, trackobj.photo.name)
            if os.path.exists(old_photo):
                os.remove(old_photo)

        trackobj.photo = photo
        trackobj.save()
        return cls.get_url()

    @classmethod
    def delete_track(cls, id):
        track = cls.objects.get(pk=id)
        if track.photo:
            photo_path = os.path.join(settings.MEDIA_ROOT, track.photo.name)
            print(f"Delete Photo: {photo_path}")
            if os.path.exists(photo_path):
                os.remove(photo_path)
                print("Photo has been Deleted")
            else:
                print("Image does not exist")

        track.delete()
        return cls.get_url()

    @classmethod
    def details_track(cls, id):
        return cls.objects.get(pk=id)