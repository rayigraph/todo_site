# Generated by Django 5.0.7 on 2024-08-28 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
