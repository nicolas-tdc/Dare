"""Models for Dare App."""

from django.db import models
from django.utils.translation import gettext_lazy as _


class Challenge(models.Model):
    """
    Model for single challenges
    """
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, default='')
    desc = models.TextField()
    nb_of_players = models.IntegerField()
    team_size = models.IntegerField()
    equipments = models.ManyToManyField(Equipment)
    proof_of_success = models.ForeignKey(ProofOfSuccess, on_delete=models.CASCADE)

    class DifficultyChoices(models.TextChoices):
        EASY = 'LO', _('Easy')
        MEDIUM = 'MD', _('Intermediate')
        HARD = 'HI', _('Hard')

    difficulty = models.CharField(
        max_length=2,
        choices=DifficultyChoices.choices,
        default=DifficultyChoices.EASY,
    )


class ChallengeCollection(models.Model):
    """
    Model for collections of single challenges.
    """
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, default='')
    desc = models.TextField()
    nb_of_players = models.IntegerField()
    challenges = models.ManyToManyField(Challenge)


class Party(models.Model):
    """
    Model for parties of players with a chosen challenge collection.
    """
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    players = models.ManyToManyField(User)
    challenge_collection = models.ForeignKey(ChallengeCollection, on_delete=models.CASCADE)


class Equipment(models.Model):
    """
    Model for equipment required for a single challenge.
    """
    name = models.CharField(max_length=100)


class ProofOfSuccess(models.Model):
    """
    Model for proof of success for an accomplished single challenge.
    """
    file = models.FileField(upload_to='TO_BE_DEFINED', editable=False)
    validations = models.IntegerField()
