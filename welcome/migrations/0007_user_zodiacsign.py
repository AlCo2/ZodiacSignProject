# Generated by Django 3.0 on 2022-08-01 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0006_remove_user_zodiacsign'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='zodiacsign',
            field=models.CharField(default='zodiacsign', max_length=20),
        ),
    ]
