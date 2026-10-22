from django import forms

GENRE_CHOICES = [
    ('all', 'Все жанры'),
    ('action', 'Боевик'),
    ('comedy', 'Комедия'),
    ('drama', 'Драма'),
    ('horror', 'Ужасы'),
    ('scifi', 'Фантастика'),
]

class GenreForm(forms.Form):
    genre = forms.ChoiceField(
        choices=GENRE_CHOICES,
        label='Выберите жанр',
        widget=forms.Select(attrs={'class': 'genre-select'}),
    )