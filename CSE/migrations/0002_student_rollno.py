# Generated by Django 4.2.7 on 2023-11-20 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='rollno',
            field=models.IntegerField(default=6100),
        ),
    ]
