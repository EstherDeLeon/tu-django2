# Generated by Django 4.1.3 on 2022-11-16 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_genre_name_bookinstance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['-id']},
        ),
    ]