# Generated by Django 4.1.5 on 2023-01-26 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apopol', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='port',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='aport/covers/'),
        ),
    ]
