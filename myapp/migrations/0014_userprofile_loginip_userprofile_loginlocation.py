# Generated by Django 4.2.6 on 2023-11-04 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_userprofile_registerlatitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='loginIP',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='loginLocation',
            field=models.TextField(default='', null=True),
        ),
    ]