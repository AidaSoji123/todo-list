# Generated by Django 4.2.7 on 2023-11-21 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_tasklist_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
