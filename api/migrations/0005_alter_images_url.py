# Generated by Django 4.1.5 on 2023-02-03 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_images_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='url',
            field=models.CharField(max_length=240),
        ),
    ]
