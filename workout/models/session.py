from django.db import models


class Session(models.Model):
    date = models.DateField()
    day = models.CharField(max_length=30, default='shanbe')
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.day
