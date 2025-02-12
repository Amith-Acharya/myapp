# Generated by Django 5.0.6 on 2024-06-10 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('languages_used', models.CharField(max_length=100)),
                ('duration', models.IntegerField(help_text='Duration in weeks')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
        ),
    ]
