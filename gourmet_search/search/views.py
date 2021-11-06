from django.shortcuts import render
from .module.hotpepper_api import get_middle_area, get_small_area, get_genre, get_shop

def index_page(request):
    result = get_middle_area()

    params = {
            "middle_area": result
    }

    return render(request, 'search/index.html', params)

def small_area(request, middle):

    result = get_small_area(middle)

    params = {
            "small_area": result,
            "middle_code" : str(middle),
    }

    return render(request, 'search/small.html', params)

def genre(request, middle, small):

    result = get_genre()

    params = {
            "genres": result,
            "middle_code" : str(middle),
            "small_code" : str(small),
    }

    return render(request, 'search/genre.html', params)

def shop(request, middle, small, genre):

    result = get_shop(middle, small, genre)

    params = {
            "middle_code" : str(middle),
            "small_code" : str(small),
            "genre_code" : str(genre),
            "shops" : result,
    }

    return render(request, 'search/shop.html', params)
