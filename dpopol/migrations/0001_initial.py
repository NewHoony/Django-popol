# Generated by Django 4.1.5 on 2023-01-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='bport/pdfs/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='bport/covers/')),
            ],
        ),
    ]
