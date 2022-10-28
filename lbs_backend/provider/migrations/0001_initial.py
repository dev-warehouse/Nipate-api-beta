# Generated by Django 4.0.6 on 2022-10-28 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProviderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Service Providers',
                'verbose_name_plural': 'Service Providers',
                'ordering': ['timeStamp'],
            },
        ),
        migrations.CreateModel(
            name='ProviderService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceTitle', models.CharField(max_length=250)),
                ('serviceDescription', models.TextField(blank=True, null=True)),
                ('ageBracket', models.CharField(blank=True, choices=[('18+', '18+'), ('All', 'All'), ('10+', '10+'), ('16+', '16+')], max_length=9, null=True)),
                ('longitude', models.CharField(blank=True, max_length=50, null=True)),
                ('lattitude', models.CharField(blank=True, max_length=50, null=True)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('centerLocationID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='providerLocation', to='locations.centerlocation')),
                ('genderID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='providerGenders', to='users.gender')),
            ],
            options={
                'verbose_name': 'Provider Services',
                'verbose_name_plural': 'Provider Services',
                'ordering': ['-timeStamp'],
            },
        ),
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(blank=True, max_length=50, null=True)),
                ('longitude', models.CharField(blank=True, max_length=50, null=True)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('requestText', models.TextField(blank=True, null=True)),
                ('centerLocationID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='locations.centerlocation')),
                ('providerServiceID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.providerservice')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_requesting', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Services Requests',
                'verbose_name_plural': 'Services Requests',
                'ordering': ['-timeStamp'],
            },
        ),
        migrations.CreateModel(
            name='ServiceResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responseText', models.TextField(blank=True, null=True)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('serviceRequestID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.servicerequest')),
            ],
            options={
                'verbose_name': 'Services Responses',
                'verbose_name_plural': 'Services Responses',
                'ordering': ['-timeStamp'],
            },
        ),
    ]
