from django.conf import settings
from django.db import models


class Date(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Thread(Date, models.Model):
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Thread {self.id}'


class Message(Date, models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']
