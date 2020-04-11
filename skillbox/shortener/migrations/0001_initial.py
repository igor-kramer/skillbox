# Generated by Django 2.2 on 2020-04-11 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='Url uid')),
                ('url', models.URLField(verbose_name='Url for shortener')),
                ('hit_count', models.IntegerField(default=0, verbose_name='Hit count')),
            ],
        ),
    ]
