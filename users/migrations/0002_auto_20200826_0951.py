# Generated by Django 3.1 on 2020-08-26 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Super Admin'), (2, 'Operation'), (3, 'Editor')], null=True),
        ),
    ]
