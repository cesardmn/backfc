from django.db import models
from django.contrib.auth.models import User
from products.models import Item


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT,
        verbose_name='Cliente'
    )
    date = models.DateField(auto_now_add=True, verbose_name='Data do pedido')
    active = models.BooleanField(default=True, verbose_name='Ativo')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f'{self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              verbose_name='Pedido', related_name='order_items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name='Quantidade')

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedido'

    def __str__(self):
        return f'{self.amount} - {self.item}'
