# Generated by Django 3.1.6 on 2021-02-02 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20210202_0817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='Pedido'),
            preserve_default=False,
        ),
    ]