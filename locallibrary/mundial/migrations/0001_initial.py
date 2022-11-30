# Generated by Django 3.2.16 on 2022-11-22 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(blank=True, max_length=100)),
                ('imagen', models.URLField(blank=True)),
                ('posicion', models.CharField(max_length=100)),
                ('equipo', models.CharField(max_length=100)),
            ],
        ),
    ]