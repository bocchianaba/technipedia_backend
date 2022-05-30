from rest_framework import serializers
from ..products import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def get_parent(self, obj):
        if obj.parent is not None:
            return ProductSerializer(obj.parent_product).data
        else:
            return None

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)

class ProductSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=[
            'id',
            'name',
            'description'
        ]

class ProductNestedSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(
        read_only=True, method_name="get_child_products")
    class Meta:
        model = Product
        fields=[
            'id',
            'name',
            'children'
        ]
    def get_child_products(self, obj):
        """ self referral field """
        serializer = ProductNestedSerializer(
            instance=obj.children_set.all(),
            many=True
        )
        return serializer.data

