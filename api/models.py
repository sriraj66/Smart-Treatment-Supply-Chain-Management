from django.db import models

class InputData(models.Model):

    gps = models.CharField(max_length=255)
    ecg = models.CharField(max_length=255)
    temp = models.CharField(max_length=255)
    humid = models.CharField(max_length=255)
    gs = models.CharField(max_length=255)
    bms = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)