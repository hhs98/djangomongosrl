from django.shortcuts import render
from rest_framework import serializers, viewsets

from .models import Deck


class DeckSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deck
        fields = '__all__'


class DecksViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = DeckSerializer
    queryset = Deck.objects.all()
