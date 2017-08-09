from rest_framework import serializers
from .models import Cars


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('id', 'manufacturer', 'model', 'age', 'color')

    def create(self, validated_data):
        return Cars.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.manufacturer = validated_data.get('manufacturer', instance.manufacturer)
        instance.model = validated_data.get('model', instance.model)
        instance.age = validated_data.get('age', instance.age)
        instance.color = validated_data.get('color', instance.color)
        instance.save()
        return instance

