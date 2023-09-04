import datetime
from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='nome')
    last_name = models.CharField(max_length=150, verbose_name='sobrenome')
    birth = models.DateField()
    photo = models.ImageField(upload_to='persons', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def age(self):
        return (datetime.date.today() - self.birth).days // 365 if self.birth is not None else None

    def __str__(self):
        return str(
            f'{self.first_name} {self.last_name} - {self.age if self.age else ""}'
        )