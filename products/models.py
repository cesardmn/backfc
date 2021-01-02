from django.db import models
from django.db.models.fields import BooleanField


class Fit(models.Model):
    name = models.TextField(
        verbose_name='nome'
    )

    price = models.DecimalField(
        verbose_name='preço',
        decimal_places=2,
        max_digits=4
    )

    active = models.BooleanField(
        default=False,
        verbose_name='ativo'
    )

    discount = models.BooleanField(
        default=False,
        verbose_name='desconto de 10%'
    )

    @property
    def sale(self):
        if self.discount == True:
            return float(self.price) * 0.9
        else:
            return float(self.price)

    @property
    def type(self):
        return 'Fit'

    def __str__(self):
        return self.name


class LowCarb(models.Model):
    name = models.TextField(
        verbose_name='nome'
    )

    price = models.DecimalField(
        verbose_name='preço',
        decimal_places=2,
        max_digits=4
    )

    active = models.BooleanField(
        default=False,
        verbose_name='ativo'
    )

    discount = models.BooleanField(
        default=False,
        verbose_name='desconto de 10%'
    )

    @property
    def sale(self):
        if self.discount == True:
            return float(self.price) * 0.9
        else:
            return float(self.price)

    @property
    def type(self):
        return 'Low Carb'

    class Meta:
        verbose_name = 'Low Carb'
        verbose_name_plural = 'Low Carbs'

    def __str__(self):
        return self.name


class Portion(models.Model):

    PORTION_CHOICES = (
        ('1', 'acompanhamentos'),
        ('2', 'carnes'),
        ('3', 'frangos'),
        ('4', 'massas'),
        ('5', 'peixes'),
    )

    type = models.CharField(
        verbose_name='tipo',
        max_length=1,
        choices=PORTION_CHOICES,
    )

    name = models.TextField(
        verbose_name='nome'
    )

    price = models.DecimalField(
        verbose_name='preço',
        decimal_places=2,
        max_digits=4
    )

    active = models.BooleanField(
        default=False,
        verbose_name='ativo'
    )

    discount = models.BooleanField(
        default=False,
        verbose_name='desconto de 10%'
    )

    @property
    def sale(self):
        if self.discount == True:
            return float(self.price) * 0.9
        else:
            return float(self.price)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Porção'
        verbose_name_plural = 'Porções'


class Combo(models.Model):
    name = models.CharField(verbose_name='nome', max_length=255)
    acompanhamentos = models.PositiveSmallIntegerField(default=0)
    carnes = models.PositiveSmallIntegerField(default=0)
    frangos = models.PositiveSmallIntegerField(default=0)
    massas = models.PositiveSmallIntegerField(default=0)
    peixe = models.PositiveSmallIntegerField(default=0)

    active = models.BooleanField(
        default=False,
        verbose_name='ativo'
    )

    def __str__(self):
        return self.name


class ItemGroup(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='grupo',
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'


class ItemType(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='tipo',
        unique=True
    )

    package = models.PositiveSmallIntegerField(
        verbose_name='embalagem (ml)'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'


class Item(models.Model):

    group = models.ForeignKey(
        ItemGroup,
        on_delete=models.CASCADE,
        verbose_name='grupo'
    )

    type = models.ForeignKey(
        ItemType,
        on_delete=models.CASCADE,
        verbose_name='tipo'
    )

    description = models.CharField(
        max_length=255,
        verbose_name='descrição'
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='preço'
    )

    active = BooleanField(
        default=False,
        verbose_name='ativo',
    )

    discount = BooleanField(
        default=False,
        verbose_name='desconto (10%)'
    )

    @property
    def full_price(self):
        return float(self.price)

    @property
    def sale_price(self):
        if self.discount == True:
            return float(self.price) * 0.9
        else:
            return float(self.price)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
