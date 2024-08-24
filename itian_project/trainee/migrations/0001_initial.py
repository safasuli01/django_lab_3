# Generated by Django 5.1 on 2024-08-23 23:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('account_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
                ('track_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='track.track')),
            ],
        ),
    ]
