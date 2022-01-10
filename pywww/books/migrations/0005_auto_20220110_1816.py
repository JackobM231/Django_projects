# Generated by Django 3.2.9 on 2022-01-10 17:16

import common.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_modified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('birth_year', models.IntegerField()),
                ('death_year', models.IntegerField(blank=True, null=True)),
                ('biogram', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, common.models.CheckAgeMixin),
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='books', to='books.Author'),
        ),
    ]