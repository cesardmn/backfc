# Generated by Django 3.1.3 on 2020-11-21 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='combo',
            name='active',
            field=models.BooleanField(default=False, verbose_name='ativo'),
        ),
    ]
