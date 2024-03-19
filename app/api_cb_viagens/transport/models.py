from django.db import models


class Transport(models.Model):
    name = models.CharField(max_length=100)
    price_confort = models.CharField(max_length=30)
    price_econ = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    duration = models.CharField(max_length=5)
    seat = models.CharField(max_length=5)
    bed = models.CharField(max_length=5)

    def __str__(self) -> str:
        return str(self.name)
