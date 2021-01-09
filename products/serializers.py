from django.db.models import fields
from rest_framework import serializers
from .models import Item, ItemGroup, ItemType


class ItemGroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = ItemGroup
        fields = ['name', 'min_order', 'description', 'image']


class ItemTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = ['name', 'package', 'menu_page']


class ItemSerializer(serializers.ModelSerializer):
    sale_price = serializers.ReadOnlyField()
    full_price = serializers.ReadOnlyField()
    group = ItemGroupSerializers(read_only=True)
    type = ItemTypeSerializers(read_only=True)

    class Meta:
        model = Item
        fields = [
            'id',
            'group',
            'type',
            'description',
            'full_price',
            'sale_price',
        ]
