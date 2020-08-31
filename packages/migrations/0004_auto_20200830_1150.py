# Generated by Django 3.1 on 2020-08-30 11:50

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0003_auto_20200827_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=80, size=[800, 533], upload_to='tours'),
        ),
    ]