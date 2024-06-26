# Generated by Django 5.0.3 on 2024-03-22 07:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_applications_employee_jobs_delete_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('can_view_applications', models.BooleanField(default=False)),
                ('can_post_jobs', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Access',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='OTP',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Token',
        ),
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.role'),
        ),
    ]
