from django.db import models
from django.forms import ModelForm
# Create your models here.

"""
    Word Model
"""
class Word(models.Model):
    english = models.CharField(max_length=30)
    german = models.CharField(max_length=30)




class WordForm(ModelForm):
    class Meta:
        model = Word
        fields= '__all__'
