# Generated by Django 3.0 on 2022-08-01 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='zodiacsign',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]