from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    schedule = models.DateTimeField()
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/')
    moderator = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    sub_category = models.CharField(max_length=255)
    rigor_rank = models.IntegerField()
    attendees = models.ManyToManyField(User, related_name='attended_events')

    def __str__(self):
        return self.name
