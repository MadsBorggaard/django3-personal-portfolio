from django.utils.timezone import now
from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    createdate = models.DateField(default=now())

    def __str__(self):
        return self.title
