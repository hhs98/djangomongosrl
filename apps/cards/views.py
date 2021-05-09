from django.shortcuts import render
from rest_framework import serializers, viewsets

from .models import Card


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'


class CardsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CardSerializer
    queryset = Card.objects.all()
