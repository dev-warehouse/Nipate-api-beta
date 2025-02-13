# Generated by Django 4.0.6 on 2022-10-28 05:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('provider', '0001_initial'),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Service Categories',
                'verbose_name_plural': 'Service Categories',
            },
        ),
        migrations.CreateModel(
            name='WorkingDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=9)),
            ],
            options={
                'verbose_name': 'Potential Working Days',
                'verbose_name_plural': 'Potential Working Days',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('categoryID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category', to='services.servicecategory')),
            ],
            options={
                'verbose_name': 'Services',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('startDate', models.DateField(default=datetime.date.today)),
                ('expiryDate', models.DateField()),
                ('noOfMessages', models.IntegerField(blank=True, null=True)),
                ('genderID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.gender')),
                ('locationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.countymodel')),
                ('providerID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='provider.providermodel')),
                ('serviceID', models.ManyToManyField(to='services.service')),
            ],
            options={
                'verbose_name': 'Advertisements',
                'verbose_name_plural': 'Advertisements',
            },
        ),
    ]
