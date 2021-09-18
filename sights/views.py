from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Category, Sight, SightImage


def sights(request):
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
    data = {
        'title': sight.title,
        'full_text': sight.full_text,
        'title_image': sight.image_preview.url,
        'img': sight_img,
        'address': sight.adress,
        'number': sight.number,
        'site': sight.site,
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
    return render(request, 'sights/show_sights.html', context=data)


def load_sights(request):
    last_sight_id = request.GET.get('lastSightId')
    category = request.GET.get('category')
    if category:
        more_sights = Sight.objects.filter(pk__gt=int(last_sight_id), category=category).values('id', 'title', 'slug', 'image_preview', 'adress')[:9]
    else:
        more_sights = Sight.objects.filter(pk__gt=int(last_sight_id)).values('id', 'title', 'slug', 'image_preview', 'adress')[:9]
    if not more_sights:
        return JsonResponse({'data': False})
    data = []
    for sight in more_sights:
        obj = {
            'id': sight['id'],
            'title': sight['title'],
            'slug': sight['slug'],
            'image_preview': sight['image_preview'],
            'address': sight['adress'],
        }
        data.append(obj)
    data[-1]['last_sight'] = True
    return JsonResponse({'data': data})
