from django.shortcuts import render, get_object_or_404
from sights.models import Sight
from sights.models import Category
from .models import PopularPeople, InterestingFact
# from django.contrib.auth.forms import UserCreationForm
from .forms import JoinForm
from django.db.models import Q


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
            # new_user.set_password(user_form.)
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
    data = {
        'title': 'Результаты поиска',
    }
    query = request.GET.get('q')
    category = Category.objects.all()
    for i in category:
        if str(i).lower() == query.lower():
            category = get_object_or_404(Category, category_name=i)
            sights = Sight.objects.filter(category=category)
            data['sights'] = sights
            return render(request, 'main/search_result.html', context=data)
            
    
    # if len(str(query)) < 5:
    #     data['ans'] = 'Ваш запрос должен состоять не менее чем из 5 символов'
    #     return render(request, 'main/search_result.html', context=data)

    # sights = Sight.objects.filter(title__iexact=query)
    # data['sights1'] = sights
    # sights = Sight.objects.filter(title__contains=query)
    # data['sights'] = sights
    # sights = Sight.objects.filter(title__iexact=query)
    # data['sights2'] = sights
    # print(sights)
    return render(request, 'main/search_result.html', context=data)