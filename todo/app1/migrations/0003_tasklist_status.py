# Generated by Django 4.2.7 on 2023-11-21 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_tasklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='status',
            field=models.CharField(default='False', max_length=20),
        ),
    ]
