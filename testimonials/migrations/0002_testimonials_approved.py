# Generated by Django 3.1 on 2020-09-29 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonials',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
