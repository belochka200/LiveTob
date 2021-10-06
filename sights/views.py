from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.viewsets import ModelViewSet
from .serializers import SightSerializer
from .models import Category, Sight, SightImage
import json

def sights(request):
    # temp = Sight.objects.all()
    # for i in temp:
    #     Sight.objects.filter(slug=i.slug).update(views=0)

    category = request.GET.get('category')
    if not category: # если категории нет
        sights_list = Sight.objects.all()[:9]
        chosen_category = ''
    else: # если категория есть
        chosen_category = get_object_or_404(Category, slug=category)
        sights_list = Sight.objects.filter(category=chosen_category)[:9]

    category_list = Category.objects.all()
    data = {
        'title': 'Достопримечательности',
        'sights_list': sights_list,
        'category_list': category_list,
        'chosen_category': chosen_category,
    }
    return render(request, 'sights/sights.html', context=data)

def show_sights(request, slug):
    sight = get_object_or_404(Sight, slug=slug)
    sight_img = SightImage.objects.filter(sight_id=sight.pk)
    sight.views += 1
    Sight.objects.filter(slug=slug).update(views=sight.views)
    if sight.views >= 1000:
        view = []
        for i in str(sight.views):
            view.append(i)
        sight_views = f'{view[0]}.{view[1]}k'
    else:
        sight_views = sight.views
    data = {
        'title': sight.title,
        'full_text': sight.full_text,
        'title_image': sight.image_preview.url,
        'img': sight_img,
        'address': sight.adress,
        'number': sight.number,
        'site': sight.site,
        'views': sight_views,
    }
    split_num = []
    temp = data['number'].split(', ')
    split_num.append(temp)
    data['number'] = split_num
    numbers = []
    for i in data['number']:
        for j in i:
            numbers.append(j)
    data['number'] = numbers
    split_address = []
    temp = data['address'].split(' / ')
    split_address.append(temp)
    data['address'] = split_address
    addresses = []
    for i in data['address']:
        for j in i:
            addresses.append(j)
    data['address'] = addresses
    return render(request, 'sights/show_sights.html', context=data)

def load_sights(request):
    last_sight_id = request.GET.get('lastSightId')
    category = request.GET.get('category')
    if category:
        more_sights = Sight.objects.filter(pk__gt=int(last_sight_id), category=category).values('id', 'title', 'slug', 'image_preview', 'adress', 'category')[:9]
    else:
        more_sights = Sight.objects.filter(pk__gt=int(last_sight_id)).values('id', 'title', 'slug', 'image_preview', 'adress', 'category')[:9]
    if not more_sights:
        return JsonResponse({'data': False})
    data = []
    for sight in more_sights:
        category = Category.objects.filter(pk=sight['category'])
        obj = {
            'id': sight['id'],
            'title': sight['title'],
            'slug': sight['slug'],
            'image_preview': sight['image_preview'],
            'address': sight['adress'],
            'category': str(category[0]),
        }
        data.append(obj)
    data[-1]['last_sight'] = True
    return JsonResponse({'data': data})

def sights_api(request):
    return render(request, 'sights/sights_api.html')

class SightsViewAPI(ModelViewSet):
    queryset = Sight.objects.all()
    serializer_class = SightSerializer
