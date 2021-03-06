# Generated by Django 3.1.3 on 2021-01-08 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_itemgroup_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemgroup',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='itemgroup',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='itemtype',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='descrição (opcional)'),
        ),
    ]
