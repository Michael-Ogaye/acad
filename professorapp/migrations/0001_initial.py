# Generated by Django 4.1.7 on 2023-03-03 20:49

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Authapp', '0010_customuser_groups_customuser_user_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('bid_date', models.DateTimeField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('rejected', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('surname', models.CharField(blank=True, max_length=30, null=True)),
                ('lastname', models.CharField(blank=True, max_length=30, null=True)),
                ('profile_picture', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='professor_images')),
                ('location', models.CharField(blank=True, max_length=90)),
                ('professor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pro_profile', to='Authapp.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_at', models.DateTimeField(auto_now_add=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('has_been_paid', models.BooleanField(default=False)),
                ('belong_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student_jobs', to='Authapp.student')),
                ('given_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='Authapp.professor')),
            ],
        ),
    ]
