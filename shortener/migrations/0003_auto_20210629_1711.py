# Generated by Django 3.2.4 on 2021-06-29 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20210629_1126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shorturl',
            old_name='redirect',
            new_name='url',
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='id',
            field=models.CharField(default='0bd69', max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
