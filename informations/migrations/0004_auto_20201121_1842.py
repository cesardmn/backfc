# Generated by Django 3.1.3 on 2020-11-21 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informations', '0003_auto_20201121_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='name',
        ),
        migrations.AddField(
            model_name='products',
            name='about',
            field=models.TextField(default='', verbose_name='sobre'),
            preserve_default=False,
        ),
    ]