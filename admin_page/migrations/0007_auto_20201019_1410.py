# Generated by Django 3.1.2 on 2020-10-19 14:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_page', '0006_auto_20201019_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='kelas',
        ),
        migrations.AddField(
            model_name='data',
            name='kelas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_page.kelas'),
        ),
    ]