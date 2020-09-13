# Generated by Django 3.1 on 2020-09-07 11:45

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0007_auto_20200831_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourItenary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='packages.tour')),
            ],
        ),
        migrations.CreateModel(
            name='TourDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=80, size=[1000, 450], upload_to='tour_detail')),
                ('image2', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=80, size=[1000, 450], upload_to='tour_detail')),
                ('image3', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=80, size=[1000, 450], upload_to='tour_detail')),
                ('description', models.TextField()),
                ('inclusion', models.TextField()),
                ('exclusion', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tour', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='packages.tour')),
            ],
        ),
    ]