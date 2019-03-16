from django.db import models

class MusicModelJAM(models.Model):
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.url


class MusicModelMobile(models.Model):
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.url
