# Generated by Django 3.2.25 on 2024-10-28 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_mcrw02', upload_to='images/'),
        ),
    ]
