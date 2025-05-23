# Generated by Django 5.1.7 on 2025-03-24 22:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0002_alter_animal_sex'),
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='animals', to='owner.owner'),
            preserve_default=False,
        ),
    ]
