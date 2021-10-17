from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import (Cafe, CafeCategory, CafeImage, Entertainment,
                     EntertainmentCategory, EntertainmentImage, Hotel,
                     HotelCategory, HotelImage)


def where_to_go(request): # all
    cafe = Cafe.objects.order_by('?')[:3]
    hotel = Hotel.objects.order_by('?')[:3]
    entertainment = Entertainment.objects.order_by('?')[:3]
    data = {
        'title': 'Куда сходить',
        'cafe': cafe,
        'hotel': hotel,
        'entertainment': entertainment,
    }
    return render(request, 'events/where_to_go.html', context=data)

def where_to_eat(request): # еда
    category = request.GET.get('category')
    category_list = CafeCategory.objects.all()
    data = {
        'title': 'Где поесть',
        'category_list': category_list,
    }
    if not category:
        chosen_category = ''
        data['chosen_category'] = chosen_category
        cafe_list_rec = Cafe.objects.filter(recomended=True)[:9] # берём рекомендованные
        if not cafe_list_rec.count() == 0:
            data['cafe_list_rec'] = cafe_list_rec
            if cafe_list_rec.count() > 9:
                return render(request, 'events/where_to_eat.html', context=data)
            else:
                x = 9-cafe_list_rec.count()
                cafe_list = Cafe.objects.filter(recomended=False)[:x]
                data['cafe_list'] = cafe_list
        else:
            cafe_list = Cafe.objects.filter(recomended=False)[:9]
            data['cafe_list'] = cafe_list
    else:
        chosen_category = get_object_or_404(CafeCategory, slug=category)
        data['chosen_category'] = chosen_category
        cafe_list_rec = Cafe.objects.filter(recomended=True, category=chosen_category)[:9]
        if not cafe_list_rec.count() == 0:
            data['cafe_list_rec'] = cafe_list_rec
            if cafe_list_rec.count() > 9:
                return render(request, 'events/where_to_eat.html', context=data)
            else:
                x = 9-cafe_list_rec.count()
                cafe_list = Cafe.objects.filter(recomended=False, category=chosen_category)[:x]
                data['cafe_list'] = cafe_list
        else:
            cafe_list = Cafe.objects.filter(recomended=False, category=chosen_category)[:9]
            data['cafe_list'] = cafe_list
    return render(request, 'events/where_to_eat.html', context=data)

def where_to_rest(request): # отдых
    category = request.GET.get('category')
    category_list = HotelCategory.objects.all()
    data = {
        'title': 'Где остановиться',
        'category_list': category_list,
    }
    if not category:
        chosen_category = ''
        data['chosen_category'] = chosen_category
        hotel_list_rec = Hotel.objects.filter(recomended=True)[:9] # берём рекомендованные
        if not hotel_list_rec.count() == 0:
            data['hotel_list_rec'] = hotel_list_rec
            if hotel_list_rec.count() > 9:
                return render(request, 'events/where_to_rest.html', context=data)
            else:
                x = 9-hotel_list_rec.count()
                hotel_list = Hotel.objects.filter(recomended=False)[:x]
                data['hotel_list'] = hotel_list
        else:
            hotel_list = Hotel.objects.filter(recomended=False)[:9]
            data['hotel_list'] = hotel_list
    else:
        chosen_category = get_object_or_404(HotelCategory, slug=category)
        data['chosen_category'] = chosen_category
        hotel_list_rec = Hotel.objects.filter(recomended=True, category=chosen_category)[:9]
        if not hotel_list_rec.count() == 0:
            data['hotel_list_rec'] = hotel_list_rec
            if hotel_list_rec.count() > 9:
                return render(request, 'events/where_to_eat.html', context=data)
            else:
                x = 9-hotel_list_rec.count()
                hotel_list = Hotel.objects.filter(recomended=False, category=chosen_category)[:x]
                data['hotel_list'] = hotel_list
        else:
            hotel_list = Hotel.objects.filter(recomended=False, category=chosen_category)[:9]
            data['hotel_list'] = hotel_list
    return render(request, 'events/where_to_rest.html', context=data)

def where_to_do(request): # куда сходить
    category = request.GET.get('category')
    category_list = EntertainmentCategory.objects.all()
    data = {
        'title': 'Чем заняться',
        'category_list': category_list,
    }
    if not category:
        chosen_category = ''
        data['chosen_category'] = chosen_category
        entertainment_list_rec = Entertainment.objects.filter(recomended=True)[:9]
        if not entertainment_list_rec == 0:
            data['entertainment_list_rec'] = entertainment_list_rec
            if entertainment_list_rec.count() > 9:
                return render(request, 'events/where_to_do.html', context=data)
            else:
                x = 9-entertainment_list_rec.count()
                entertainment_list = Entertainment.objects.filter(recomended=False)[:x]
                data['entertainment_list'] = entertainment_list
        else:
            entertainment_list = Entertainment.objects.filter(recomended=False)[:9]
            data['entertainment_list'] = entertainment_list
    else:
        chosen_category = get_object_or_404(EntertainmentCategory, slug=category)
        entertainment_list_rec = Entertainment.objects.filter(recomended=True, category=chosen_category)[:9]
        if not entertainment_list_rec.count() == 0:
            data['entertainment_list_rec'] = entertainment_list_rec
            if entertainment_list_rec.count() > 9:
                return render(request, 'events/where_to_do.html', context=data)
            else:
                x = 9-entertainment_list_rec.count()
                entertainment_list = Entertainment.objects.filter(recomended=False, category=chosen_category)[:x]
                data['entertainment_list'] = entertainment_list
        else:
            entertainment_list = Entertainment.objects.filter(recomended=False, category=chosen_category)[:9]
            data['entertainment_list'] = entertainment_list
    return render(request, 'events/where_to_do.html', context=data)


def cafe_load(request):
    lastid = request.GET.get('lastid')
    lastrecid = request.GET.get('lastrecid')
    category = request.GET.get('category')
    data = []
    if category: # если есть категория
        if lastrecid: # если есть идшник рек. карточки
            more_cafe_rec = Cafe.objects.filter(pk__gt=int(lastrecid), recomended=True, category=category).values(
                'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:9]        
            if not more_cafe_rec: # если больше нет реков
                more_cafe = Cafe.objects.filter(pk__gt=int(lastid), recomended=False, category=category).values(
                    'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:9]
                if more_cafe:
                    for item in more_cafe:
                        category = CafeCategory.objects.filter(pk=item['category'])
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                            'category': str(category[0]),
                        }
                        data.append(obj)
                    data[-1]['last-post-eat'] = True
                    return JsonResponse({'data': data})
                else:
                    return JsonResponse({'data': False})
            else: # если реки есть
                for item in more_cafe_rec:
                    category = CafeCategory.objects.filter(pk=item['category'])
                    obj_rec = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
                        'category': str(category[0]),
                    }
                    data.append(obj_rec)
                x = 9-more_cafe_rec.count()
                more_cafe = Cafe.objects.filter(pk__gt=int(lastid), recomended=False, category=category).values(
                    'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:x]
                if more_cafe:
                    for item in more_cafe:
                        category = CafeCategory.objects.filter(pk=item['category'])
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                            'category': str(category[0]),
                        }
                        data.append(obj)
                    data[-1]['last-post-eat'] = True
                    return JsonResponse({'data': data})
                else:
                    data[-1]['last-post-eat'] = True
                    return JsonResponse({'data': data})
        else: # если нет идшника реков последнего
            more_cafe = Cafe.objects.filter(pk__gt=int(lastid), recomended=False, category=category).values(
                'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:9]
            if more_cafe:
                for item in more_cafe:
                    category = CafeCategory.objects.filter(pk=item['category'])
                    obj = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
                        'category': str(category[0]),
                    }
                    data.append(obj)
                data[-1]['last-post-eat'] = True
                return JsonResponse({'data': data})
            else:
                return JsonResponse({'data': False})
    else: # если нет категории
        if lastrecid: # если есть идшник рек. карточки
            more_cafe_rec = Cafe.objects.filter(pk__gt=int(lastrecid), recomended=True).values(
                'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:9]        
            if not more_cafe_rec: # если больше нет реков
                more_cafe = Cafe.objects.filter(pk__gt=int(lastid), recomended=False).values(
                    'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:9]
                if more_cafe:
                    for item in more_cafe:
                        category = CafeCategory.objects.filter(pk=item['category'])
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                            'category': str(category[0]),
                        }
                        data.append(obj)
                    data[-1]['last-post-eat'] = True
                    return JsonResponse({'data': data})
                else:
                    return JsonResponse({'data': False})
            else: # если реки есть
                for item in more_cafe_rec:
                    category = CafeCategory.objects.filter(pk=item['category'])
                    obj_rec = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
                        'category': str(category[0]),
                    }
                    data.append(obj_rec)
                x = 9-more_cafe_rec.count()
                more_cafe = Cafe.objects.filter(pk__gt=int(lastid), recomended=False).values(
                    'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:x]
                if more_cafe:
                    for item in more_cafe:
                        category = CafeCategory.objects.filter(pk=item['category'])
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                            'category': str(category[0]),
                        }
                        data.append(obj)
                    data[-1]['last-post-eat'] = True
                    return JsonResponse({'data': data})
                else:
                    for item in more_cafe_rec:
                        category = CafeCategory.objects.filter(pk=item['category'])
                        obj_rec = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                            'category': str(category[0]),
                        }
                        data.append(obj_rec)
                    data[-1]['last-post-eat'] = True
                    return JsonResponse({'data': data})
        else: # если нет идшника реков последнего
            more_cafe = Cafe.objects.filter(pk__gt=int(lastid), recomended=False).values(
                'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:9]
            if more_cafe:
                for item in more_cafe:
                    category = CafeCategory.objects.filter(pk=item['category'])
                    obj = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
                        'category': str(category[0]),
                    }
                    data.append(obj)
                data[-1]['last-post-eat'] = True
                return JsonResponse({'data': data})
            else:
                return JsonResponse({'data': False})

def hotel_load(request):
    lastid = request.GET.get('lastid')
    lastrecid = request.GET.get('lastrecid')
    category = request.GET.get('category')
    data = []
    if category: # если есть категория
        if lastrecid: # если есть идшник рек. карточки
            more_hotels_rec = Hotel.objects.filter(pk__gt=int(lastrecid), recomended=True, category=category).values(
                'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:9]        
            if not more_hotels_rec: # если больше нет реков
                more_hotels = Hotel.objects.filter(pk__gt=int(lastid), recomended=False, category=category).values(
                    'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:9]
                if more_hotels:
                    for item in more_hotels:
                        category = CafeCategory.objects.filter(pk=item['category'])
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                            'category': str(category[0]),
                        }
                        data.append(obj)
                    data[-1]['last-post-rest'] = True
                    return JsonResponse({'data': data})
                else:
                    return JsonResponse({'data': False})
            else: # если реки есть
                for item in more_hotels_rec:
                    category = CafeCategory.objects.filter(pk=item['category'])
                    obj_rec = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
                        'category': str(category[0]),
                    }
                    data.append(obj_rec)
                x = 9-more_hotels_rec.count()
                more_hotels = Hotel.objects.filter(pk__gt=int(lastid), recomended=False, category=category).values(
                    'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:x]
                if more_hotels:
                    for item in more_hotels:
                        category = CafeCategory.objects.filter(pk=item['category'])
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                            'category': str(category[0]),
                        }
                        data.append(obj)
                    data[-1]['last-post-rest'] = True
                    return JsonResponse({'data': data})
                else:
                    data[-1]['last-post-rest'] = True
                    return JsonResponse({'data': data})
        else: # если нет идшника реков последнего
            more_hotels = Hotel.objects.filter(pk__gt=int(lastid), recomended=False, category=category).values(
                'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:9]
            if more_hotels:
                for item in more_hotels:
                    category = CafeCategory.objects.filter(pk=item['category'])
                    obj = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
                        'category': str(category[0]),
                    }
                    data.append(obj)
                data[-1]['last-post-rest'] = True
                return JsonResponse({'data': data})
            else:
                return JsonResponse({'data': False})
    else: # если нет категории
        if lastrecid: # если есть идшник рек. карточки
            more_hotels_rec = Hotel.objects.filter(pk__gt=int(lastrecid), recomended=True).values(
                'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:9]        
            if not more_hotels_rec: # если больше нет реков
                more_hotels = Hotel.objects.filter(pk__gt=int(lastid), recomended=False).values(
                    'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:9]
                if more_hotels:
                    for item in more_hotels:
                        category = CafeCategory.objects.filter(pk=item['category'])
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                            'category': str(category[0]),
                        }
                        data.append(obj)
                    data[-1]['last-post-rest'] = True
                    return JsonResponse({'data': data})
                else:
                    return JsonResponse({'data': False})
            else: # если реки есть
                for item in more_hotels_rec:
                    category = CafeCategory.objects.filter(pk=item['category'])
                    obj_rec = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
                        'category': str(category[0]),
                    }
                    data.append(obj_rec)
                x = 9-more_hotels_rec.count()
                more_hotels = Hotel.objects.filter(pk__gt=int(lastid), recomended=False).values(
                    'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:x]
                if more_hotels:
                    for item in more_hotels:
                        category = CafeCategory.objects.filter(pk=item['category'])
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                            'category': str(category[0]),
                        }
                        data.append(obj)
                    data[-1]['last-post-rest'] = True
                    return JsonResponse({'data': data})
                else:
                    for item in more_hotels_rec:
                        category = CafeCategory.objects.filter(pk=item['category'])
                        obj_rec = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                            'category': str(category[0]),
                        }
                        data.append(obj_rec)
                    data[-1]['last-post-rest'] = True
                    return JsonResponse({'data': data})
        else: # если нет идшника реков последнего
            more_hotels = Hotel.objects.filter(pk__gt=int(lastid), recomended=False).values(
                'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:9]
            if more_hotels:
                for item in more_hotels:
                    category = CafeCategory.objects.filter(pk=item['category'])
                    obj = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
                        'category': str(category[0]),
                    }
                    data.append(obj)
                data[-1]['last-post-rest'] = True
                return JsonResponse({'data': data})
            else:
                return JsonResponse({'data': False})
                
def ent_load(request):
    lastid = request.GET.get('lastid')
    lastrecid = request.GET.get('lastrecid')
    category = request.GET.get('category')
    data = []
    if category: # если есть категория
        if lastrecid: # если есть идшник рек. карточки
            more_ent_rec = Entertainment.objects.filter(pk__gt=int(lastrecid), recomended=True, category=category).values(
                'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:9]        
            if not more_ent_rec: # если больше нет реков
                more_ent = Entertainment.objects.filter(pk__gt=int(lastid), recomended=False, category=category).values(
                    'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:9]
                if more_ent:
                    for item in more_ent:
                        category = EntertainmentCategory.objects.filter(pk=item['category'])
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                            'category': str(category[0]),
                        }
                        data.append(obj)
                    data[-1]['last-post-rest'] = True
                    return JsonResponse({'data': data})
                else:
                    return JsonResponse({'data': False})
            else: # если реки есть
                for item in more_ent_rec:
                    category = EntertainmentCategory.objects.filter(pk=item['category'])
                    obj_rec = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
                        'category': str(category[0])
                    }
                    data.append(obj_rec)
                x = 9-more_ent_rec.count()
                more_ent = Entertainment.objects.filter(pk__gt=int(lastid), recomended=False, category=category).values(
                    'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:x]
                if more_ent:
                    for item in more_ent:
                        category = EntertainmentCategory.objects.filter(pk=item['category'])
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                            'category': str(category[0]),
                        }
                        data.append(obj)
                    data[-1]['last-post-rest'] = True
                    return JsonResponse({'data': data})
                else:
                    data[-1]['last-post-rest'] = True
                    return JsonResponse({'data': data})
        else: # если нет идшника реков последнего
            more_ent = Entertainment.objects.filter(pk__gt=int(lastid), recomended=False, category=category).values(
                'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:9]
            if more_ent:
                for item in more_ent:
                    category = EntertainmentCategory.objects.filter(pk=item['category'])
                    obj = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
                        'category': str(category[0]),
                    }
                    data.append(obj)
                data[-1]['last-post-rest'] = True
                return JsonResponse({'data': data})
            else:
                return JsonResponse({'data': False})
    else: # если нет категории
        if lastrecid: # если есть идшник рек. карточки
            more_ent_rec = Entertainment.objects.filter(pk__gt=int(lastrecid), recomended=True).values(
                'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:9]        
            if not more_ent_rec: # если больше нет реков
                more_ent = Entertainment.objects.filter(pk__gt=int(lastid), recomended=False).values(
                    'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:9]
                if more_ent:
                    for item in more_ent:
                        category = EntertainmentCategory.objects.filter(pk=item['category'])
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                            'category': str(category[0])
                        }
                        data.append(obj)
                    data[-1]['last-post-to-do'] = True
                    return JsonResponse({'data': data})
                else:
                    return JsonResponse({'data': False})
            else: # если реки есть
                for item in more_ent_rec:
                    category = EntertainmentCategory.objects.filter(pk=item['category'])
                    obj_rec = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
                        'category': str(category[0]),
                    }
                    data.append(obj_rec)
                x = 9-more_ent_rec.count()
                more_ent = Hotel.objects.filter(pk__gt=int(lastid), recomended=False).values(
                    'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:x]
                if more_ent:
                    for item in more_ent:
                        category = EntertainmentCategory.objects.filter(pk=item['category'])
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                            'category': str(category[0]),
                        }
                        data.append(obj)
                    data[-1]['last-post-to-do'] = True
                    return JsonResponse({'data': data})
                else:
                    for item in more_ent_rec:
                        category = EntertainmentCategory.objects.filter(pk=item['category'])
                        obj_rec = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                            'category': str(category[0]),
                        }
                        data.append(obj_rec)
                    data[-1]['last-post-to-do'] = True
                    return JsonResponse({'data': data})
        else: # если нет идшника реков последнего
            more_ent = Hotel.objects.filter(pk__gt=int(lastid), recomended=False).values(
                'id', 'title', 'slug', 'image_preview', 'address', 'recomended', 'category')[:9]
            if more_ent:
                for item in more_ent:
                    category = EntertainmentCategory.objects.filter(pk=item['category'])
                    obj = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
                        'category': str(category[0]),
                    }
                    data.append(obj)
                data[-1]['last-post-to-do'] = True
                return JsonResponse({'data': data})
            else:
                return JsonResponse({'data': False})


def show_to_eat(request, slug):
    cafe = get_object_or_404(Cafe, slug=slug)
    cafe_img = CafeImage.objects.filter(cafe=cafe.pk)
    cafe.views += 1
    Cafe.objects.filter(slug=slug).update(views=cafe.views)
    if cafe.views >= 1000:
        view = []
        for i in str(cafe.views):
            view.append(i)
        cafe_views = f'{view[0]}.{view[1]}k'
    else:
        cafe_views = cafe.views
    data = {
        'title': cafe.title,
        'description': cafe.description,
        'title_image': cafe.image_preview.url,
        'img': cafe_img,
        'address': cafe.address,
        'number': cafe.number,
        'site': cafe.site,
        'views': cafe_views,
    }
    if data['number']:
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

    more = Cafe.objects.order_by('?').filter(category=cafe.category)[:3]
    n = 0
    temp = []
    for i in more:
        more = get_object_or_404(Cafe, title=i)
        temp.append([])
        temp[n].append(more.title)
        temp[n].append(more.image_preview.url)
        temp[n].append(more.slug)
        temp[n].append(more.category)
        temp[n].append(more.address)
        n += 1
    data['more'] = temp
    temp = []
    temp.append(data['more'][0][3])
    category = get_object_or_404(CafeCategory, category_name=temp[0])
    temp.append(category.slug)
    data['category'] = temp
    data['type'] = 'eat'
    return render(request, 'main/show.html', context=data)

def show_to_rest(request, slug):
    rest = get_object_or_404(Hotel, slug=slug)
    rest_img = HotelImage.objects.filter(hotel=rest.pk)
    rest.views += 1
    Hotel.objects.filter(slug=slug).update(views=rest.views)
    if rest.views >= 1000:
        view = []
        for i in str(rest.views):
            view.append(i)
        rest_views = f'{view[0]}.{view[1]}k'
    else:
        rest_views = rest.views
    data = {
        'title': rest.title,
        'description': rest.description,
        'title_image': rest.image_preview.url,
        'img': rest_img,
        'address': rest.address,
        'number': rest.number,
        'site': rest.site,
        'views': rest_views,
    }
    if data['number']:
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

    more = Hotel.objects.order_by('?').filter(category=rest.category)[:3]
    n = 0
    temp = []
    for i in more:
        more = get_object_or_404(Hotel, title=i)
        temp.append([])
        temp[n].append(more.title)
        temp[n].append(more.image_preview.url)
        temp[n].append(more.slug)
        temp[n].append(more.category)
        temp[n].append(more.address)
        n += 1
    data['more'] = temp
    temp = []
    temp.append(data['more'][0][3])
    category = get_object_or_404(HotelCategory, category_name=temp[0])
    temp.append(category.slug)
    data['category'] = temp
    data['type'] = 'rest'
    return render(request, 'main/show.html', context=data)

def show_to_do(request, slug):
    do = get_object_or_404(Entertainment, slug=slug)
    do_img = EntertainmentImage.objects.filter(ent=do.pk)
    do.views += 1
    Entertainment.objects.filter(slug=slug).update(views=do.views)
    if do.views >= 1000:
        view = []
        for i in str(do.views):
            view.append(i)
        do_views = f'{view[0]}.{view[1]}k'
    else:
        do_views = do.views
    data = {
        'title': do.title,
        'description': do.description,
        'title_image': do.image_preview.url,
        'img': do_img,
        'address': do.address,
        'number': do.number,
        'site': do.site,
        'views': do_views,
        'price': do.price,
    }
    if data['number']:
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

    more = Entertainment.objects.order_by('?').filter(category=do.category)[:3]
    n = 0
    temp = []
    for i in more:
        more = get_object_or_404(Entertainment, title=i)
        temp.append([])
        temp[n].append(more.title)
        temp[n].append(more.image_preview.url)
        temp[n].append(more.slug)
        temp[n].append(more.category)
        temp[n].append(more.address)
        n += 1
    data['more'] = temp
    temp = []
    temp.append(data['more'][0][3])
    category = get_object_or_404(EntertainmentCategory, category_name=temp[0])
    temp.append(category.slug)
    data['category'] = temp
    data['type'] = 'ent'
    return render(request, 'main/show.html', context=data)
