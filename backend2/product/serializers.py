from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url) if request else obj.image.url

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'image']
