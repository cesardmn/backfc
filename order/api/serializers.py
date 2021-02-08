from django.db.models import fields
from rest_framework import serializers
from order.models import Order, OrderItem
from products.models import Item
# from django.contrib.auth.models import User


class ItemSerializer(serializers.ModelSerializer):
    sale_price = serializers.ReadOnlyField()

    class Meta:
        model = Item
        fields = ('id', 'description', 'sale_price')


class OrderItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ('amount', 'item')


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):

        order = super().create(validated_data)
        order_items = self.initial_data['orderItems']

        for order_item in order_items:
            OrderItem.objects.create(
                order=order,
                item=Item.objects.get(id=order_item['item']),
                amount=order_item['amount']
            )
        return order
