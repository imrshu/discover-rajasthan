# Generated by Django 3.1 on 2021-01-12 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0022_auto_20201101_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourdetail',
            name='price',
        ),
    ]
