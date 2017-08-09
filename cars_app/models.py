from django.db import models

# Create your models here.


class Cars(models.Model):

    class Meta(object):
        verbose_name = "Car"
        verbose_name_plural = "Cars"
        ordering = ['-datetime']

    manufacturer = models.CharField(
        max_length=256,
        blank=False
    )

    model = models.CharField(
        max_length=256,
        blank=False
    )

    age = models.PositiveIntegerField()

    color = models.CharField(
        max_length=256,
        blank=False
    )

    datetime = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return "{}-{}".format(self.manufacturer, self.model)
