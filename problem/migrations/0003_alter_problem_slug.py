# Generated by Django 4.2.5 on 2023-09-11 14:47

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0002_alter_problem_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True),
        ),
    ]
