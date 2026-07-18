from rest_framework import serializers
from .models import Match
from .models import MatchPlayer

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'status']

class MatchPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchPlayer
        fields='__all__'
