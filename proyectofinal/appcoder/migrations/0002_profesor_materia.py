# Generated by Django 4.0.4 on 2022-05-10 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='Materia',
            field=models.CharField(default=3, max_length=255),
            preserve_default=False,
        ),
    ]
