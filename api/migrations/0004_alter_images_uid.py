# Generated by Django 4.1.5 on 2023-02-03 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_user_id_generation_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='uid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
