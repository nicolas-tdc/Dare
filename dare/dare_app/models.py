from django.db import models
from django.utils.translation import gettext_lazy as _


class Challenge(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, default='')
    desc = models.TextField()
    nb_of_players = models.IntegerField()
    team_size = models.IntegerField()
    equipments = models.ManyToManyField(Equipment)
    proof_of_success = models.FileField(upload_to='TO_BE_DEFINED', editable=False)

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
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, default='')
    desc = models.TextField()
    nb_of_players = models.IntegerField()


class Party(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    players = models.ManyToManyField(User)
    challenges_group = models.ForeignKey(ChallengeCollection, on_delete=models.CASCADE)


class Equipment(models.Model):
    name = models.CharField(max_length=100)
