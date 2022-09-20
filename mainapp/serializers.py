from rest_framework.serializers import ModelSerializer
from .models import Travel


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Travel
        fields = '__all__'