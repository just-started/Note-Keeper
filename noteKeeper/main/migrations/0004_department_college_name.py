# Generated by Django 3.0.7 on 2020-06-15 04:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_college'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='college_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]