# Generated by Django 3.1 on 2021-01-19 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0023_remove_tourdetail_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourdetail',
            name='keywords',
            field=models.TextField(blank=True, null=True),
        ),
    ]
