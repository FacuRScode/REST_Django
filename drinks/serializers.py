from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):


    #describir el modelo
    #es lo que tenemos en form?
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']