# Generated by Django 3.2.15 on 2022-09-14 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220914_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Group Rides', max_length=50),
        ),
    ]