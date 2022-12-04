from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField('Car Name', max_length=40)
    price = models.IntegerField('Price')
    img = models.CharField('Image Here', default=None, max_length=400)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'