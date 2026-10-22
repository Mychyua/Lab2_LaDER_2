from django.shortcuts import render
from .forms import GenreForm

MOVIES = [
    {'title': 'Мстители: Финал', 'title_en': 'Avengers: Endgame', 'genre': 'action', 'year': 2019, 'description': 'Эпическая битва супергероев против Таноса за судьбу вселенной.', 'description_en': 'Epic battle of superheroes against Thanos for the fate of the universe.', 'image': 'images/avengers_endgame.jpg', 'video_url': 'https://www.youtube.com/watch?v=TcMBFSGVi1c'},
    {'title': 'Джон Уик', 'title_en': 'John Wick', 'genre': 'action', 'year': 2014, 'description': 'Легендарный наёмный убийца выходит на тропу войны после гибели собаки.', 'description_en': 'A legendary hitman goes on a warpath after the death of his dog.', 'image': 'images/john_wick.jpg', 'video_url': 'https://www.youtube.com/watch?v=C0BMx-qxsP4'},
    {'title': 'Безумный Макс: Дорога ярости', 'title_en': 'Mad Max: Fury Road', 'genre': 'action', 'year': 2015, 'description': 'Постапокалиптический экшен в пустыне с погонями и взрывами.', 'description_en': 'Post-apocalyptic action in the desert with chases and explosions.', 'image': 'images/mad_max.jpg', 'video_url': 'https://www.youtube.com/watch?v=hEJnMQG9ev8'},
    {'title': 'Один дома', 'title_en': 'Home Alone', 'genre': 'comedy', 'year': 1990, 'description': 'Мальчик остаётся один на Рождество и защищает дом от грабителей.', 'description_en': 'A boy is left alone at Christmas and defends his home from burglars.', 'image': 'images/home_alone.jpg', 'video_url': 'https://www.youtube.com/watch?v=jEDaVHmw7r4'},
    {'title': 'Мальчишник в Вегасе', 'title_en': 'The Hangover', 'genre': 'comedy', 'year': 2009, 'description': 'Три друга ищут пропавшего жениха после безумной ночи в Вегасе.', 'description_en': 'Three friends search for a missing groom after a wild night in Vegas.', 'image': 'images/hangover.jpg', 'video_url': 'https://www.youtube.com/watch?v=tcdUhdOlz9M'},
    {'title': 'Маска', 'title_en': 'The Mask', 'genre': 'comedy', 'year': 1994, 'description': 'Скромный банковский клерк находит маску, превращающую его в супергероя.', 'description_en': 'A shy bank clerk finds a mask that turns him into a superhero.', 'image': 'images/the_mask.jpg', 'video_url': 'https://www.youtube.com/watch?v=LZl69yk5lEY'},
    {'title': 'Побег из Шоушенка', 'title_en': 'The Shawshank Redemption', 'genre': 'drama', 'year': 1994, 'description': 'Банкир, осуждённый за убийство, планирует дерзкий побег из тюрьмы.', 'description_en': 'A banker convicted of murder plans a daring escape from prison.', 'image': 'images/shawshank.jpg', 'video_url': 'https://www.youtube.com/watch?v=6hB3S9bIaco'},
    {'title': 'Зелёная миля', 'title_en': 'The Green Mile', 'genre': 'drama', 'year': 1999, 'description': 'История о сверхъестественных способностях заключённого в камере смертников.', 'description_en': 'A story about the supernatural abilities of a death row inmate.', 'image': 'images/green_mile.jpg', 'video_url': 'https://www.youtube.com/watch?v=Ki4haFrqSrw'},
    {'title': 'Форрест Гамп', 'title_en': 'Forrest Gump', 'genre': 'drama', 'year': 1994, 'description': 'Простодушный мужчина становится свидетелем ключевых событий XX века.', 'description_en': 'A simple-minded man witnesses key events of the 20th century.', 'image': 'images/forrest_gump.jpg', 'video_url': 'https://www.youtube.com/watch?v=bLvqoHBptjg'},
    {'title': 'Сияние', 'title_en': 'The Shining', 'genre': 'horror', 'year': 1980, 'description': 'Писатель сходит с ума в изоляции зимнего отеля под влиянием злых сил.', 'description_en': 'A writer goes mad in the isolation of a winter hotel under the influence of evil forces.', 'image': 'images/the_shining.jpg', 'video_url': 'https://www.youtube.com/watch?v=5Cb3ik6zP2I'},
    {'title': 'Заклятие', 'title_en': 'The Conjuring', 'genre': 'horror', 'year': 2013, 'description': 'Семья сталкивается с демонической активностью в своём новом доме.', 'description_en': 'A family encounters demonic activity in their new home.', 'image': 'images/conjuring.jpg', 'video_url': 'https://www.youtube.com/watch?v=k10ETZ41q5o'},
    {'title': 'Астрал', 'title_en': 'Insidious', 'genre': 'horror', 'year': 2010, 'description': 'Мальчик впадает в кому, и его душа попадает в мир духов.', 'description_en': 'A boy falls into a coma and his soul enters the spirit world.', 'image': 'images/insidious.jpg', 'video_url': 'https://www.youtube.com/watch?v=zuZnRUcoWos'},
    {'title': 'Интерстеллар', 'title_en': 'Interstellar', 'genre': 'scifi', 'year': 2014, 'description': 'Астронавты путешествуют сквозь червоточину в поисках новой планеты.', 'description_en': 'Astronauts travel through a wormhole in search of a new planet.', 'image': 'images/interstellar.jpg', 'video_url': 'https://www.youtube.com/watch?v=zSWdZVtXT7E'},
    {'title': 'Начало', 'title_en': 'Inception', 'genre': 'scifi', 'year': 2010, 'description': 'Вор проникает в сны людей, чтобы украсть их секреты.', 'description_en': 'A thief enters people\'s dreams to steal their secrets.', 'image': 'images/inception.jpg', 'video_url': 'https://www.youtube.com/watch?v=YoHD9XEInc0'},
    {'title': 'Матрица', 'title_en': 'The Matrix', 'genre': 'scifi', 'year': 1999, 'description': 'Хакер узнаёт, что реальность — это компьютерная симуляция.', 'description_en': 'A hacker discovers that reality is a computer simulation.', 'image': 'images/matrix.jpg', 'video_url': 'https://www.youtube.com/watch?v=vKQi3bBA1y8'},
]

GENRE_NAMES = {
    'ru': {'action': 'Боевик', 'comedy': 'Комедия', 'drama': 'Драма', 'horror': 'Ужасы', 'scifi': 'Фантастика', 'all': 'Все жанры'},
    'en': {'action': 'Action', 'comedy': 'Comedy', 'drama': 'Drama', 'horror': 'Horror', 'scifi': 'Sci-Fi', 'all': 'All genres'},
}

TEXTS = {
    'ru': {'site_title': 'Онлайн-кинотеатр', 'heading': 'Выберите фильм по жанру', 'submit': 'Показать', 'theme_label': 'Тема:', 'lang_label': 'Язык:', 'light': 'Светлая', 'dark': 'Тёмная', 'no_movies': 'Фильмы не найдены.', 'year': 'Год', 'recent': 'Последние страницы:', 'watch_trailer': 'Смотреть трейлер'},
    'en': {'site_title': 'Online Cinema', 'heading': 'Choose a movie by genre', 'submit': 'Show', 'theme_label': 'Theme:', 'lang_label': 'Language:', 'light': 'Light', 'dark': 'Dark', 'no_movies': 'No movies found.', 'year': 'Year', 'recent': 'Recent pages:', 'watch_trailer': 'Watch trailer'},
}

def index(request):
    theme = request.COOKIES.get('theme', 'light')
    lang = request.COOKIES.get('lang', 'ru')
    recent_raw = request.COOKIES.get('recent_pages', '')

    if 'set_theme' in request.GET:
        new_theme = request.GET['set_theme']
        if new_theme in ('light', 'dark'):
            theme = new_theme
    if 'set_lang' in request.GET:
        new_lang = request.GET['set_lang']
        if new_lang in ('ru', 'en'):
            lang = new_lang

    form = GenreForm(request.GET or None)
    selected_genre = 'all'
    if form.is_valid():
        selected_genre = form.cleaned_data['genre']

    if selected_genre == 'all':
        movies = MOVIES
    else:
        movies = [m for m in MOVIES if m['genre'] == selected_genre]

    t = TEXTS.get(lang, TEXTS['ru'])
    genre_names = GENRE_NAMES.get(lang, GENRE_NAMES['ru'])

    movies_with_display = []
    for m in movies:
        dm = dict(m)
        if lang == 'en':
            dm['display_title'] = m.get('title_en', m['title'])
            dm['display_description'] = m.get('description_en', m['description'])
        else:
            dm['display_title'] = m['title']
            dm['display_description'] = m['description']
        dm['display_genre'] = genre_names.get(m['genre'], m['genre'])
        movies_with_display.append(dm)

    recent_pages_raw = [p for p in recent_raw.split(',') if p] if recent_raw else []
    recent_pages = []
    for p in recent_pages_raw:
        genre_key = p.replace('genre=', '')
        display_name = genre_names.get(genre_key, genre_key)
        recent_pages.append({'url': p, 'display': display_name})

    current_page = f'genre={selected_genre}'
    current_display = genre_names.get(selected_genre, selected_genre)

    recent_pages = [p for p in recent_pages if p['url'] != current_page]
    recent_pages.insert(0, {'url': current_page, 'display': current_display})
    recent_pages = recent_pages[:5]

    context = {
        'form': form,
        'movies': movies_with_display,
        'theme': theme,
        'lang': lang,
        't': t,
        'genre_names': genre_names,
        'recent_pages': recent_pages,
        'selected_genre': selected_genre,
    }

    response = render(request, 'movies/index.html', context)
    response.set_cookie('theme', theme, max_age=30*24*3600)
    response.set_cookie('lang', lang, max_age=30*24*3600)
    response.set_cookie('recent_pages', ','.join([p['url'] for p in recent_pages]), max_age=30*24*3600)

    return response