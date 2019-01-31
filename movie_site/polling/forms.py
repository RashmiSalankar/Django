from django import forms
from .models import Movie
from .models import User

class MovieForm(forms.ModelForm):
    class Meta:
        movie_model = Movie
        fields = [
            'title',
            'total_likes'
        ]
