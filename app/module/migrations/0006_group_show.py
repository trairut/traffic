# Generated by Django 4.2.4 on 2023-08-28 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0005_rename_status_focus_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]
