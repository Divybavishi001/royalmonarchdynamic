# Generated by Django 5.0.3 on 2024-03-20 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=100, null=True)),
                ('Last_Name', models.CharField(max_length=100, null=True)),
                ('Email', models.EmailField(max_length=200, null=True)),
                ('Mobile', models.CharField(max_length=10, null=True)),
                ('Comments', models.TextField(max_length=2000, null=True)),
            ],
        ),
    ]
