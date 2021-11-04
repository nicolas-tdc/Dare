from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from dare_app.models import (
    Challenge, ChallengeCollection, Party, Equipment, ProofOfSuccess,
)
from dare_app.serializers import (
    UserSerializer, GroupSerializer, ChallengeSerializer, ChallengeCollectionSerializer,
    PartySerializer, EquipmentSerializer, ProofOfSuccessSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChallengeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows challenges to be viewed or edited
    """
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChallengeCollectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows challenge collections to be viewed or edited
    """
    queryset = ChallengeCollection.objects.all()
    serializer_class = ChallengeCollectionSerializer
    permission_classes = [permissions.IsAuthenticated]


class PartyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows parties to be viewed or edited
    """
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    permissions_classes = [permissions.IsAuthenticated]


class EquipmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows equipments to be viewed or edited
    """
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProofOfSuccessViewSet(viewsets.ModelViewSet):
    """
    API endoint that allows equipments to be viewed or edited
    """
    queryset = ProofOfSuccess.objects.all()
    serializer_class = ProofOfSuccessSerializer
    permission_classes = [permissions.IsAuthenticated]
