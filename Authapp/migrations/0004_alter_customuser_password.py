# Generated by Django 4.1.7 on 2023-02-27 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authapp', '0003_customuser_date_joined_customuser_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=150),
        ),
    ]
