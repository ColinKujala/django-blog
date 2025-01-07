from django.db import models

class Poll(models.Model):
    title = models.CharField(max_length=128)
    text = models.CharField(blank=True, max_length=512)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title
