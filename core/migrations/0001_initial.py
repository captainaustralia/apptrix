# Generated by Django 4.0.3 on 2022-03-30 12:14

import core.funcs
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('avatar', models.ImageField(blank=True, default='/default.png', upload_to=core.funcs.get_file_path)),
                ('longitude', models.FloatField(blank=True, default=0)),
                ('latitude', models.FloatField(blank=True, default=0)),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who_liked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who', to=settings.AUTH_USER_MODEL)),
                ('who_was_liked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='whose', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='liked',
            field=models.ManyToManyField(through='core.Membership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='participant',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
