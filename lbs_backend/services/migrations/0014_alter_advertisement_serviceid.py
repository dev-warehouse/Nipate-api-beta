# Generated by Django 4.0.6 on 2022-10-08 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0013_rename_adtext_advertisement_addescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='ServiceID',
            field=models.ManyToManyField(to='services.service'),
        ),
    ]
