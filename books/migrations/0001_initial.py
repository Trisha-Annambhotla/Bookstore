# Generated by Django 5.0.6 on 2024-05-30 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=50)),
                ('Publication_year', models.IntegerField()),
                ('Genre', models.CharField(max_length=30)),
                ('Availibity', models.BooleanField()),
            ],
        ),
    ]
