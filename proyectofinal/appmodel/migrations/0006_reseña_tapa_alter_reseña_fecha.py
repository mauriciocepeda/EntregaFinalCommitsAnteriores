# Generated by Django 4.0.4 on 2022-05-27 22:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appmodel', '0005_alter_reseña_cuerpo'),
    ]

    operations = [
        migrations.AddField(
            model_name='reseña',
            name='tapa',
            field=models.ImageField(default=4, upload_to='tapas'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reseña',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
