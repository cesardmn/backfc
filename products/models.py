from django.db import models


class ItemGroup(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='grupo',
        unique=True
    )

    min_order = models.SmallIntegerField(
        verbose_name='pedido mínimo'
    )

    description = models.TextField(
        verbose_name='descrição',
        null=True,
        blank=True
    )

    image = models.ImageField(
        verbose_name='imagem do grupo'
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
        verbose_name='embalagem (ml)',
        null=True,
        blank=True
    )

    description = models.TextField(
        verbose_name='descrição (opcional)',
        null=True,
        blank=True
    )

    menu_page = models.PositiveSmallIntegerField(
        verbose_name='página do cardápio'
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

    description = models.TextField(
        verbose_name='descrição'
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='preço'
    )

    active = models.BooleanField(
        default=False,
        verbose_name='ativo',
    )

    discount = models.BooleanField(
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
