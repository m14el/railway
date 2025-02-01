from django.db import models


class Wagon(models.Model):
    train_number = models.CharField(max_length=50)
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    wagon_number = models.CharField(max_length=50)
    waybill_number = models.CharField(max_length=50)
    cargo = models.CharField(max_length=100)
    weight = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.train_number} - {self.wagon_number}'