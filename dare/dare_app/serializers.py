"""API Serializers for Dare App"""


from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Challenge, ChallengeCollection, Party, Equipment, ProofOfSuccess


class ChallengeSerializer(serializers.HyperlinkedModelSerializer):
    """
    API Serializer for single challenges.
    """
    class Meta:
        model = Challenge
        fields = [
            'id', 'created', 'author', 'title', 'desc', 'nb_of_players',
            'team_size', 'equipments', 'proof_of_success', 'difficulty',
        ]


class ChallengeCollectionSerializer(serializers.HyperlinkedModelSerializer):
    """
    API Serializer for collections of single challenges.
    """
    class Meta:
        model = ChallengeCollection
        fields = ['created', 'author', 'title', 'desc', 'nb_of_players']


class PartySerializer(serializers.HyperlinkedModelSerializer):
    """
    API Serializer for parties of players with a chosen challenge collection.
    """
    class Meta:
        model = Party
        fields = ['admin', 'players', 'challenge_collection']


class EquipmentSerializer(serializers.HyperlinkedModelSerializer):
    """
    API Serializer for equipment required for a single challenge
    """
    class Meta:
        model = Equipment
        fields = ['name']


class ProofOfSuccessSerializer(serializers.HyperlinkedModelSerializer):
    """
    API Serializer for proof of success for an accomplished single challenge.
    """
    class Meta:
        model = ProofOfSuccess
        fields = ['file', 'validations']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    API Serializer for app users.
    """
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    API Serializer for group of app users.
    """
    class Meta:
        model = Group
        fields = ['url', 'name']
