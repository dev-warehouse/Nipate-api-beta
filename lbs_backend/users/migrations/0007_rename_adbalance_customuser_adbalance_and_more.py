# Generated by Django 4.0.6 on 2022-10-28 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customuser_locationid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='ADBalance',
            new_name='adBalance',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='DateCreated',
            new_name='dateCreated',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='FirstName',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='GenderID',
            new_name='genderID',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='IDNumber',
            new_name='idNumber',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='LocationID',
            new_name='locationID',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='MiddleName',
            new_name='middleName',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='MobileNumber',
            new_name='mobileNumber',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='SurName',
            new_name='surName',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='YearOfBirth',
            new_name='yearOfBirth',
        ),
    ]
