# Generated by Django 4.1.1 on 2022-12-14 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_listing_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.CharField(default='', max_length=500),
        ),
    ]