# Generated by Django 5.0.3 on 2024-03-21 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_testimonials'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonials',
            name='Sub_Feedback',
            field=models.CharField(max_length=100, null=True),
        ),
    ]