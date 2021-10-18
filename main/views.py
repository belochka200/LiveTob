from django.shortcuts import render
from events.models import *
from sights.models import *

from .forms import JoinForm
from .models import *


def index(request): # главная страница
    sights_list = Sight.objects.all()[:3]
    popular_people = PopularPeople.objects.all()
    interesting_facts = InterestingFact.objects.all()
    data = {
        'title': 'Live Tob',
        'sights': 'Достопримечательности',
        'sights_list': sights_list,
        'popular_people': popular_people,
        'interesting_facts': interesting_facts,
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

def developers(request):
    data = {
        'title': 'API LiveTob | Разработчикам'
    }
    return render(request, 'main/developers.html', context=data)

def brand(request):
    data = {
        'title': 'Ресурсы LiveTob'
    }
    return render(request, 'main/brand.html', context=data)

def join(request):
    if request.method == 'POST':
        user_form = JoinForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
        
            new_user.save()
    data = {
        'title': 'Присоединиться к LiveTob',
        'form': user_form,
    }
    return render(request, 'main/join.html', context=data)

def login(request):
    data = {
        'title': 'Войти в LiveTob',
    }
    return render(request, 'main/login.html', context=data)

def search(request):
    '''
    Костыль. Исправить, перенести БД на MySQL, переписать весь поиск
    '''
    query = request.GET.get('q')
    query_split = query[:-2]
    data = {
        'title': 'Результаты поиска',
        'query': query,
    }
    # category = Category.objects.all()
    # for i in category:
    #     if str(i).lower() == str(query).lower():
    #         categoryList = []
    #         category = get_object_or_404(Category, category_name=i)
    #         categoryList.append(category)
    #         category = get_object_or_404(CafeCategory, category_name=i)
    #         categoryList.append(category)
    #         category = get_object_or_404(HotelCategory, category_name=i)
    #         categoryList.append(category)
    #         category = get_object_or_404(EntertainmentCategory, category_name=i)

    #         sights = Sight.objects.filter(category=data['sights'])
    #         rest = Hotel.objects.filter(category=data['rest'])
    #         data['sights'] = sights
    #         return render(request, 'main/search_result.html', context=data)
            
    sights = Sight.objects.all()
    rest = Hotel.objects.all()
    cafe = Cafe.objects.all()
    do = Entertainment.objects.all()
    data['sights'] = []
    data['sights2'] = []
    data['rest'] = []
    data['rest2'] = []
    data['cafe'] = []
    data['cafe2'] = []
    data['do'] = []
    data['do2'] = []
    for i in sights:
        if str(query).lower() in str(i.title).lower():
            data['sights'].append([i.title, i.image_preview, i.slug, i.adress, i.category])
        if str(query).lower() in str(i.full_text).lower():
            data['sights2'].append([i.title, i.image_preview, i.slug, i.adress, i.category])

    for i in rest:
        if str(query).lower() in str(i.title).lower():
            data['rest'].append([i.title, i.image_preview, i.slug, i.address, i.category])
        if str(query).lower() in str(i.description).lower():
            data['rest2'].append([i.title, i.image_preview, i.slug, i.address, i.category])
    
    for i in cafe:
        if str(query).lower() in str(i.title).lower():
            data['cafe'].append([i.title, i.image_preview, i.slug, i.address, i.category])
        if str(query).lower() in str(i.description).lower():
            data['cafe2'].append([i.title, i.image_preview, i.slug, i.address, i.category])

    for i in do:
        if str(query).lower() in str(i.title).lower():
            data['do'].append([i.title, i.image_preview, i.slug, i.address, i.category])
        if str(query).lower() in str(i.description).lower():
            data['do2'].append([i.title, i.image_preview, i.slug, i.address, i.category])

    return render(request, 'main/search_result.html', context=data)
