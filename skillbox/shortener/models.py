import uuid
from django.db import models


class Link(models.Model):
    id = models.CharField('Url uid', max_length=8, primary_key=True)
    url = models.URLField(verbose_name='Url for shortener')
    hit_count = models.IntegerField('Hit count', default=0)

    def __str__(self):
        return f'{ self.id } { self.url } ({ self.hit_count } hits)'

    def inc_hits(self):
        self.hit_count += 1
        self.save()


