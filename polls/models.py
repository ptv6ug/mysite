from django.db import models


class Message(models.Model):
    message_text = models.CharField(max_length=200)
