from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Challenge, ChallengesGroup, Party, Equipment


class ChallengeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Challenge
        fields = [
            'id', 'created', 'author', 'title', 'desc', 'nb_of_players',
            'team_size', 'equipments', 'proof_of_success', 'difficulty',
        ]


class ChallengesGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChallengesGroup
        fields = ['created', 'author', 'title', 'desc', 'nb_of_players']


class PartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Party
        fields = ['admin', 'players', 'challenge_group']


class EquipmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Equipment
        fields = ['name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
