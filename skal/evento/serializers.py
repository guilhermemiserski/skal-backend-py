from rest_framework import serializers
from .models import Evento, Ingresso

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingresso
        fields = '__all__'
    