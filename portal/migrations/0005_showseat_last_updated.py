# Generated by Django 4.2 on 2023-04-20 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_remove_seat_theatre_seat_screen'),
    ]

    operations = [
        migrations.AddField(
            model_name='showseat',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]