# Generated by Django 4.0.4 on 2022-06-21 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoGallary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multipleimages', models.FileField(blank=True, null=True, upload_to='galleries')),
            ],
        ),
    ]
