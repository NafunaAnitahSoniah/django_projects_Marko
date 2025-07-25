# Generated by Django 5.2.4 on 2025-07-21 21:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('duedate', models.DateField()),
                ('priority', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=15)),
                ('creationdate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
