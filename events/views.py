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
            more_cafe_rec = Cafe.objects.filter(pk__gt=int(lastrecid), recomended=True, category=category).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:9]        
            if not more_cafe_rec: # если больше нет реков
                more_cafe = Cafe.objects.filter(pk__gt=int(lastid), recomended=False, category=category).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:9]
                if more_cafe:
                    for item in more_cafe:
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                        }
                        data.append(obj)
                    data[-1]['last-post-eat'] = True
                    return JsonResponse({'data': data})
                else:
                    return JsonResponse({'data': False})
            else: # если реки есть
                for item in more_cafe_rec:
                    obj_rec = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
                    }
                    data.append(obj_rec)
                x = 9-more_cafe_rec.count()
                more_cafe = Cafe.objects.filter(pk__gt=int(lastid), recomended=False, category=category).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:x]
                if more_cafe:
                    for item in more_cafe:
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                        }
                        data.append(obj)
                    data[-1]['last-post-eat'] = True
                    return JsonResponse({'data': data})
                else:
                    data[-1]['last-post-eat'] = True
                    return JsonResponse({'data': data})
        else: # если нет идшника реков последнего
            more_cafe = Cafe.objects.filter(pk__gt=int(lastid), recomended=False, category=category).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:9]
            if more_cafe:
                for item in more_cafe:
                    obj = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
                    }
                    data.append(obj)
                data[-1]['last-post-eat'] = True
                return JsonResponse({'data': data})
            else:
                return JsonResponse({'data': False})
    else: # если нет категории
        if lastrecid: # если есть идшник рек. карточки
            more_cafe_rec = Cafe.objects.filter(pk__gt=int(lastrecid), recomended=True).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:9]        
            if not more_cafe_rec: # если больше нет реков
                more_cafe = Cafe.objects.filter(pk__gt=int(lastid), recomended=False).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:9]
                if more_cafe:
                    for item in more_cafe:
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                        }
                        data.append(obj)
                    data[-1]['last-post-eat'] = True
                    return JsonResponse({'data': data})
                else:
                    return JsonResponse({'data': False})
            else: # если реки есть
                for item in more_cafe_rec:
                    obj_rec = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
                    }
                    data.append(obj_rec)
                x = 9-more_cafe_rec.count()
                more_cafe = Cafe.objects.filter(pk__gt=int(lastid), recomended=False).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:x]
                if more_cafe:
                    for item in more_cafe:
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                        }
                        data.append(obj)
                    data[-1]['last-post-eat'] = True
                    return JsonResponse({'data': data})
                else:
                    for item in more_cafe_rec:
                        obj_rec = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                        }
                        data.append(obj_rec)
                    data[-1]['last-post-eat'] = True
                    return JsonResponse({'data': data})
        else: # если нет идшника реков последнего
            more_cafe = Cafe.objects.filter(pk__gt=int(lastid), recomended=False).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:9]
            if more_cafe:
                for item in more_cafe:
                    obj = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
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
            more_hotels_rec = Hotel.objects.filter(pk__gt=int(lastrecid), recomended=True, category=category).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:9]        
            if not more_hotels_rec: # если больше нет реков
                more_hotels = Hotel.objects.filter(pk__gt=int(lastid), recomended=False, category=category).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:9]
                if more_hotels:
                    for item in more_hotels:
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                        }
                        data.append(obj)
                    data[-1]['last-post-rest'] = True
                    return JsonResponse({'data': data})
                else:
                    return JsonResponse({'data': False})
            else: # если реки есть
                for item in more_hotels_rec:
                    obj_rec = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
                    }
                    data.append(obj_rec)
                x = 9-more_hotels_rec.count()
                more_hotels = Hotel.objects.filter(pk__gt=int(lastid), recomended=False, category=category).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:x]
                if more_hotels:
                    for item in more_hotels:
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                        }
                        data.append(obj)
                    data[-1]['last-post-rest'] = True
                    return JsonResponse({'data': data})
                else:
                    data[-1]['last-post-rest'] = True
                    return JsonResponse({'data': data})
        else: # если нет идшника реков последнего
            more_hotels = Hotel.objects.filter(pk__gt=int(lastid), recomended=False, category=category).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:9]
            if more_hotels:
                for item in more_hotels:
                    obj = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
                    }
                    data.append(obj)
                data[-1]['last-post-rest'] = True
                return JsonResponse({'data': data})
            else:
                return JsonResponse({'data': False})
    else: # если нет категории
        if lastrecid: # если есть идшник рек. карточки
            more_hotels_rec = Hotel.objects.filter(pk__gt=int(lastrecid), recomended=True).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:9]        
            if not more_hotels_rec: # если больше нет реков
                more_hotels = Hotel.objects.filter(pk__gt=int(lastid), recomended=False).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:9]
                if more_hotels:
                    for item in more_hotels:
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                        }
                        data.append(obj)
                    data[-1]['last-post-rest'] = True
                    return JsonResponse({'data': data})
                else:
                    return JsonResponse({'data': False})
            else: # если реки есть
                for item in more_hotels_rec:
                    obj_rec = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
                    }
                    data.append(obj_rec)
                x = 9-more_hotels_rec.count()
                more_hotels = Hotel.objects.filter(pk__gt=int(lastid), recomended=False).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:x]
                if more_hotels:
                    for item in more_hotels:
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                        }
                        data.append(obj)
                    data[-1]['last-post-rest'] = True
                    return JsonResponse({'data': data})
                else:
                    for item in more_hotels_rec:
                        obj_rec = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                        }
                        data.append(obj_rec)
                    data[-1]['last-post-rest'] = True
                    return JsonResponse({'data': data})
        else: # если нет идшника реков последнего
            more_hotels = Hotel.objects.filter(pk__gt=int(lastid), recomended=False).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:9]
            if more_hotels:
                for item in more_hotels:
                    obj = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
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
            more_ent_rec = Entertainment.objects.filter(pk__gt=int(lastrecid), recomended=True, category=category).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:9]        
            if not more_ent_rec: # если больше нет реков
                more_ent = Entertainment.objects.filter(pk__gt=int(lastid), recomended=False, category=category).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:9]
                if more_ent:
                    for item in more_ent:
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                        }
                        data.append(obj)
                    data[-1]['last-post-rest'] = True
                    return JsonResponse({'data': data})
                else:
                    return JsonResponse({'data': False})
            else: # если реки есть
                for item in more_ent_rec:
                    obj_rec = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
                    }
                    data.append(obj_rec)
                x = 9-more_ent_rec.count()
                more_ent = Entertainment.objects.filter(pk__gt=int(lastid), recomended=False, category=category).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:x]
                if more_ent:
                    for item in more_ent:
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                        }
                        data.append(obj)
                    data[-1]['last-post-rest'] = True
                    return JsonResponse({'data': data})
                else:
                    data[-1]['last-post-rest'] = True
                    return JsonResponse({'data': data})
        else: # если нет идшника реков последнего
            more_ent = Entertainment.objects.filter(pk__gt=int(lastid), recomended=False, category=category).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:9]
            if more_ent:
                for item in more_ent:
                    obj = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
                    }
                    data.append(obj)
                data[-1]['last-post-rest'] = True
                return JsonResponse({'data': data})
            else:
                return JsonResponse({'data': False})
    else: # если нет категории
        if lastrecid: # если есть идшник рек. карточки
            more_ent_rec = Entertainment.objects.filter(pk__gt=int(lastrecid), recomended=True).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:9]        
            if not more_ent_rec: # если больше нет реков
                more_ent = Entertainment.objects.filter(pk__gt=int(lastid), recomended=False).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:9]
                if more_ent:
                    for item in more_ent:
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                        }
                        data.append(obj)
                    data[-1]['last-post-to-do'] = True
                    return JsonResponse({'data': data})
                else:
                    return JsonResponse({'data': False})
            else: # если реки есть
                for item in more_ent_rec:
                    obj_rec = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
                    }
                    data.append(obj_rec)
                x = 9-more_ent_rec.count()
                more_ent = Hotel.objects.filter(pk__gt=int(lastid), recomended=False).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:x]
                if more_ent:
                    for item in more_ent:
                        obj = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                        }
                        data.append(obj)
                    data[-1]['last-post-to-do'] = True
                    return JsonResponse({'data': data})
                else:
                    for item in more_ent_rec:
                        obj_rec = {
                            'id': item['id'],
                            'title': item['title'],
                            'slug': item['slug'],
                            'image_preview': item['image_preview'],
                            'address': item['address'],
                            'recomended': item['recomended'],
                        }
                        data.append(obj_rec)
                    data[-1]['last-post-to-do'] = True
                    return JsonResponse({'data': data})
        else: # если нет идшника реков последнего
            more_ent = Hotel.objects.filter(pk__gt=int(lastid), recomended=False).values('id', 'title', 'slug', 'image_preview', 'address', 'recomended')[:9]
            if more_ent:
                for item in more_ent:
                    obj = {
                        'id': item['id'],
                        'title': item['title'],
                        'slug': item['slug'],
                        'image_preview': item['image_preview'],
                        'address': item['address'],
                        'recomended': item['recomended'],
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
        'recomended': cafe.recomended,
        'views': cafe_views,
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
    return render(request, 'events/show_to_eat.html', context=data)

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
        'recomended': rest.recomended,
        'views': rest_views,
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
    return render(request, 'events/show_to_rest.html', context=data)

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
        'recomended': do.recomended,
        'views': do_views,
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
    return render(request, 'events/show_to_do.html', context=data)
