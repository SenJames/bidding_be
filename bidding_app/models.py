from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime
# Create your models here.


class Staff(models.Model):
    user = models.CharField(max_length=255)
    identity = models.UUIDField(default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50)
    gifted = models.BooleanField(default=False)
    giver = models.BooleanField(default=True)

    class Meta:
        verbose_name = "staff"
        verbose_name_plural = "staff"

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_photo = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=None)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)
    count = models.IntegerField()

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Bid(models.Model):
    item = models.ForeignKey(
        Item, verbose_name="Item", on_delete=models.CASCADE)
    giver = models.OneToOneField(
        "Staff", verbose_name="Staff", on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.now)
    recipient = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Bid"
        verbose_name_plural = "Bids"

    def __str__(self):
        return self.item.item_name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
