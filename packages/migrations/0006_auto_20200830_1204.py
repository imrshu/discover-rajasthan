# Generated by Django 3.1 on 2020-08-30 12:04

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0005_auto_20200830_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=80, size=[1920, 1080], upload_to='category'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=80, size=[1920, 1080], upload_to='tours'),
        ),
    ]
