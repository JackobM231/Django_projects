# Generated by Django 3.2.9 on 2022-03-10 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_post_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategoria', 'verbose_name_plural': 'Kategorie'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posty'},
        ),
    ]
