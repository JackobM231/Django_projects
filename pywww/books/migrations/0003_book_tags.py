# Generated by Django 3.2.9 on 2022-01-10 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('books', '0002_alter_book_publication_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(related_name='books', to='tags.Tag'),
        ),
    ]
