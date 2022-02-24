# Generated by Django 3.2.9 on 2022-02-22 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='source',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]