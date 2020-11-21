# Generated by Django 3.1.3 on 2020-11-21 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_one', models.TextField(verbose_name='parágrafo 1')),
                ('info_two', models.TextField(verbose_name='parágrafo 2')),
            ],
            options={
                'verbose_name': 'sobre',
                'verbose_name_plural': 'sobre',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whatsapp', models.CharField(max_length=9, verbose_name='WhatsApp')),
                ('instagram', models.CharField(max_length=255, verbose_name='Instagram')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_one', models.TextField(verbose_name='parágrafo 1')),
                ('info_two', models.TextField(verbose_name='parágrafo 2')),
            ],
            options={
                'verbose_name': 'Entrega',
                'verbose_name_plural': 'Entrega',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_one', models.TextField(verbose_name='parágrafo 1')),
                ('info_two', models.TextField(verbose_name='parágrafo 2')),
            ],
            options={
                'verbose_name': 'Encomendas',
                'verbose_name_plural': 'Encomendas',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(choices=[('C', 'combo'), ('L', 'marmita')], max_length=1, verbose_name='sobre')),
                ('about', models.TextField(verbose_name='sobre')),
                ('amount', models.CharField(max_length=4, verbose_name='quantidade (ml)')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos  ',
            },
        ),
    ]