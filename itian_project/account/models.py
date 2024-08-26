from django.db import models
from django.urls import reverse
import os
from django.conf import settings

#Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    add_to = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='account/photos', null=True, blank=True)

    @staticmethod
    def get_url():
        return reverse('account_list')

    def getimage(self):
        return f"/media/{self.photo}"

    @classmethod
    def getall(cls):
        return [
            (
                account.id,
                account.username,
                account.email,
                account.password,
                account.add_to,
                account.photo
            )
            for account in cls.objects.all()
        ]

    @classmethod
    def create_account(cls, username, email, password,photo):
        accountobj = cls()
        accountobj.username = username
        accountobj.email = email
        accountobj.password = password
        accountobj.photo = photo
        accountobj.save()
        return cls.get_url()

    @classmethod
    def update_account(cls, id, email, password, photo, username):
        accountobj = cls.objects.get(pk=id)
        accountobj.username = username
        accountobj.email = email
        accountobj.password = password
        if photo and accountobj.photo and accountobj.photo != photo:
            old_photo = os.path.join(settings.MEDIA_ROOT,accountobj.photo.name)
            if os.path.exists(old_photo):
                os.remove(old_photo)
        accountobj.photo = photo
        accountobj.save()
        return cls.get_url()

    @classmethod
    def delete_account(cls, id):
        accountobj = cls.objects.get(pk=id)
        if accountobj.image:
            photo = os.path.join(settings.MEDIA_ROOT, accountobj.photo.name)
            print(f"Delete Photo: {photo}")
            if os.path.exists(photo):
                os.remove(photo)
                print("Photo is Deleted")
            else:
                print("Photo does not exist")

        accountobj.delete()
        return cls.get_url()

    @classmethod
    def details_account(cls, id):
        return cls.objects.get(pk=id)

