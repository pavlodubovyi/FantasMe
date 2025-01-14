from django import forms
from .models import PlayerCharacter, CharacterClass


class PlayerCharacterForm(forms.ModelForm):
    character_class = forms.ModelChoiceField(
        queryset=CharacterClass.objects.all(),
        empty_label="Select a character class",
        label="Character Class"
    )

    class Meta:
        model = PlayerCharacter
        fields = ['name', 'character_class', 'face']
