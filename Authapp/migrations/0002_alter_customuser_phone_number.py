# Generated by Django 4.1.7 on 2023-02-27 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
