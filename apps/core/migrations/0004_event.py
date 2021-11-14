# Generated by Django 3.2.9 on 2021-11-14 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_eat_map_detail_seatmapdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_team', models.CharField(max_length=255)),
                ('guest_team', models.CharField(max_length=255)),
                ('event_date', models.DateTimeField(blank=True, null=True)),
                ('event_time', models.DateTimeField(blank=True, null=True)),
                ('stadiom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stadiom', to='core.stadiom')),
            ],
        ),
    ]
