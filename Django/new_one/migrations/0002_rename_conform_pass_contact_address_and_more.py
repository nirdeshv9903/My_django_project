# Generated by Django 4.2.7 on 2023-11-26 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_one', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='conform_pass',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='firstname',
            new_name='date_of_birth',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='lastname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='password',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='username',
            new_name='second_add',
        ),
    ]
