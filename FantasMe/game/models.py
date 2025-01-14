from django.db import models


class CharacterClass(models.Model):
    name = models.CharField(max_length=50)
    evolution_level = models.IntegerField()
    aggression = models.IntegerField()
    compassion = models.IntegerField()
    law_respect = models.IntegerField()
    luck = models.IntegerField()
    open_mind = models.IntegerField()

    def __str__(self):
        return self.name


class PlayerCharacter(models.Model):
    name = models.CharField(max_length=50)
    character_class = models.ForeignKey('CharacterClass', on_delete=models.CASCADE)
    face = models.ImageField(upload_to='faces/', default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
