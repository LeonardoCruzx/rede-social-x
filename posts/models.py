from django.db import models

from cloudinary.models import CloudinaryField



class Post(models.Model):
    autor = models.ForeignKey(
        'users.User',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    date_update = models.TimeField(
        auto_now_add=True,
        null=False,
        blank=False
    )
    title = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )
    description = models.TextField(
        max_length=250,
        null=True,
        blank=True
    )
    image = CloudinaryField(
        "post_pictures/post_picture",
        null=True,
        blank=True
    )
    comments = models.PositiveIntegerField(
        default=0,
        null=False,
        blank=False
    )
    likes = models.PositiveIntegerField(
        default=0,
        null=False,
        blank=False
    )
    shares = models.PositiveIntegerField(
        default=0,
        null=False,
        blank=False
    )
    def __str__(self):
        return str(self.pk)