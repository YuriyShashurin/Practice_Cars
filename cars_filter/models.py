from django.db import models

# Create your models here.
class Car(models.Model):

    TRANSMISSION = [
        (1, 'Механика'),
        (2, 'Автомат'),
        (3, 'Робот'),
    ]
    COLOR = [
        (1, 'Черный'),
        (2, 'Красный'),
        (3, 'Белый'),
        (4, 'Мокрый асфальт'),
        (5, 'Желтый'),
    ]

    creater = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year_create = models.IntegerField()
    transmission = models.SmallIntegerField(choices=TRANSMISSION)
    color = models.SmallIntegerField(choices=COLOR)
    photo = models.ImageField(upload_to='cars_photo/', blank=True,)


    def __str__(self):
        a = str('{} - {} - {}'.format(self.creater, self.model, self.year_create))
        return a
