# Generated by Django 3.2.4 on 2021-06-29 08:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='hit_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='id',
            field=models.CharField(default=uuid.UUID('e61c8529-7944-4911-bffc-ee0754f61e89'), max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
