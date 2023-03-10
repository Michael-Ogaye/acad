# Generated by Django 4.1.7 on 2023-03-08 21:20

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='files',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='task_files'),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='studentapp.taskcategory'),
        ),
    ]
