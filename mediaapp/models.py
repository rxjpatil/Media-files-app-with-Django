# media_app/models.py
from django.db import models

class MediaManager(models.Manager):
    def audio(self):
        return self.filter(type='audio')

    def video(self):
        return self.filter(type='video')

    def images(self):
        return self.filter(type='image')

class Media(models.Model):
    MEDIA_TYPES = (
        ('audio', 'Audio'),
        ('video', 'Video'),
        ('image', 'Image'),
    )

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    format = models.CharField(max_length=10)
    size = models.PositiveIntegerField()
    duration_secs = models.IntegerField(default=0)

    objects = MediaManager()

    def __str__(self):
        return self.name
