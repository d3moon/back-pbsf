from rest_framework import serializers
from .models import Vacina

class VacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = ['id', 'nome', 'publico_alvo']

    def create(self, validated_data):
        return Vacina.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.publico_alvo = validated_data.get('publico_alvo', instance.publico_alvo)
        instance.save()
        return instance
