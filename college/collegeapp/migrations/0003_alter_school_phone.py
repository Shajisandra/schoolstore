# Generated by Django 4.2.2 on 2023-08-10 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0002_alter_school_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
