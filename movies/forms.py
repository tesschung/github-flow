from django import forms
from .models import Movie, Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['content', 'score', ]