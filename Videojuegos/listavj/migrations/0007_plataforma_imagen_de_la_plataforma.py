# Generated by Django 2.0.2 on 2018-03-09 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listavj', '0006_auto_20180309_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='plataforma',
            name='imagen_de_la_plataforma',
            field=models.ImageField(blank=True, null=True, upload_to='plataformas'),
        ),
    ]
