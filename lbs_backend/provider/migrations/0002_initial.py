# Generated by Django 4.0.6 on 2022-10-28 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('provider', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0001_initial'),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='providerservice',
            name='productID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='providerProductID', to='services.service'),
        ),
        migrations.AddField(
            model_name='providerservice',
            name='providerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='providerID', to='provider.providermodel'),
        ),
        migrations.AddField(
            model_name='providerservice',
            name='workingDays',
            field=models.ManyToManyField(related_name='workingdays', to='services.workingdays'),
        ),
        migrations.AddField(
            model_name='providermodel',
            name='countyID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provider_county', to='locations.countymodel'),
        ),
        migrations.AddField(
            model_name='providermodel',
            name='userID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='UserProviderID', to=settings.AUTH_USER_MODEL),
        ),
    ]
