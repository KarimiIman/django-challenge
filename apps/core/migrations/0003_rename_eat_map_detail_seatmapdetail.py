# Generated by Django 3.2.9 on 2021-11-14 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_seat_map_detail_eat_map_detail'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='eat_map_detail',
            new_name='SeatMapDetail',
        ),
    ]
