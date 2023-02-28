# Generated by Django 4.1.7 on 2023-02-27 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authapp', '0004_alter_customuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=65),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='type',
            field=models.CharField(choices=[('STUDENT', 'student'), ('PROFESSOR', 'professor'), ('C_ADMIN', 'c_admin')], default='C_ADMIN', max_length=40),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]