# Generated by Django 3.1 on 2020-08-30 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0004_auto_20200830_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tours'),
        ),
    ]
