from django.shortcuts import render
from sights.models import Sight


def index(request): # главная страница
    sights_list = Sight.objects.all()[:3]
    data = {
        'title': 'Live Tob',
        'sights': 'Достопримечательности',
        # 'page_title': 'Главная',
        'sights_list': sights_list,
    }
    return render(request, 'main/index.html', context=data)

def about(request): # страница "о нас"
    data = {
        'title': 'О нас',
    }
    return render(request, 'main/about.html', context=data)

def history(request): # история города
    data = {
        'title': 'История города',
    }
    return render(request, 'main/history.html', context=data)

# def load(request):
#     return render(request, 'main/load.html')

def developers(request):
    data = {
        'title': 'API LiveTob | Разработчикам'
    }
    # response = requests.get('http://127.0.0.1:8000/api/sights/?format=json')
    # response = response.json()
    # for i in response:
    #     print(f'Название: {i["title"]} | Категория: {i["category"]}')
        # print(i['title'])
    # print(response)
    return render(request, 'main/developers.html', context=data)

def brand(request):
    data = {
        'title': 'Ресурсы LiveTob'
    }
    return render(request, 'main/brand.html', context=data)