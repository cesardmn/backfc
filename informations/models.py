from django.db import models


class About(models.Model):
    info_one = models.TextField(
        verbose_name='parágrafo 1'
    )

    info_two = models.TextField(
        verbose_name='parágrafo 2'
    )

    class Meta:
        verbose_name = 'sobre'
        verbose_name_plural = 'sobre'

    def __str__(self):
        return 'Sobre'


class Products(models.Model):
    PRODUCTS_CHOICES = (
        ('combo', 'Combo Caseiro'),
        ('fit', 'Marmita Fit'),
        ('lowcarb', 'Marmita Low Carb'),
    )

    product = models.CharField(
        max_length=255,
        choices=PRODUCTS_CHOICES,
        blank=False,
        null=False,
        verbose_name='tipo'
    )

    about = models.TextField(
        verbose_name='sobre'
    )

    amount = models.CharField(
        max_length=4,
        verbose_name='quantidade (ml)'
    )

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos  '

    def __str__(self):
        return self.product


class Contact(models.Model):

    whatsapp = models.CharField(
        max_length=9,
        verbose_name='WhatsApp'
    )

    instagram = models.CharField(
        max_length=255,
        verbose_name='Instagram'
    )

    email = models.EmailField()

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.email


class Delivery(models.Model):
    info_one = models.TextField(
        verbose_name='parágrafo 1'
    )

    info_two = models.TextField(
        verbose_name='parágrafo 2'
    )

    class Meta:
        verbose_name = 'Entrega'
        verbose_name_plural = 'Entrega'

    def __str__(self):
        return 'Entregas'


class Order(models.Model):
    info_one = models.TextField(
        verbose_name='parágrafo 1'
    )

    info_two = models.TextField(
        verbose_name='parágrafo 2'
    )

    class Meta:
        verbose_name = 'Encomendas'
        verbose_name_plural = 'Encomendas'

    def __str__(self):
        return 'Encomendas'
