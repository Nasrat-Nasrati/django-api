# In Django, serializers are used in Django REST Framework (DRF) to convert complex data types like Django models into JSON format (for APIs), and also validate and convert JSON data back into Python objects.

# 🔹 In short:
# Serializers = Translators between Django models and JSON (or other formats) for APIs.

from rest_framework import serializers
from reporting.models import Orders
class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
        
