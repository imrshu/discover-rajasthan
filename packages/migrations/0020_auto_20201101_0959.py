# Generated by Django 3.1 on 2020-11-01 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0019_tour_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourdetail',
            name='num_of_days',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tourdetail',
            name='num_of_nights',
            field=models.PositiveIntegerField(default=0),
        ),
    ]