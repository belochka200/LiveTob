$(document).ready(function() {
    $('.btn__show-more-eat').click(function() {
        let lastid = $('.last-post-eat').attr('data-postid')
        let lastrecid = $('.last-post-eat').attr('data-postidrec')
        let category = $('.chosen_category').attr('data-categoryid')
        let data = { 
            lastid: lastid,
            lastrecid: lastrecid,
            category: category
        }
        $('.posts-eat').removeClass('last-post-eat')
        $('.posts-eat').removeAttr('data-postid')
        $('.posts-eat').removeAttr('data-postidrec')
        let url = $('.btn__show-more-eat').attr('btn-url')
        $.ajax({
            method: "GET",
            dataType: "json",
            url: url,
            data: data,
            success: function(data) {
                let res = data['data']
                if (!res) {
                    $('.btn__show-more-eat').fadeOut('slow')
                    $('.no-more').css('display', 'none')
                    $('.no-more').text('Нам нечего показать')
                    $('.no-more').delay(1000).fadeIn('slow')
                    $('.no-more').append('<br><i class="far fa-frown"></i>')
                } else {
                    if ($('body').hasClass('dark-theme')) {
                        $.each(res, function(key, obj) {
                            if (obj['last-post-eat']) {
                                if (obj['recomended']) {
                                    $('.all-eat').append(
                                        '<div class="col-12 col-md-4 posts-eat last-post-eat dark-theme" data-postid="0" data-postidrec="' + obj['id'] + '">' + 
                                            '<a href="show-to-eat-' + obj['slug'] + '" class="dark-theme">' + 
                                                '<div class="card mt-5 dark-theme">' + 
                                                    '<img src="../../media/' + obj['image_preview'] + '" class="card-img-top round dark-theme">' + 
                                                    '<div class="rec-card dark-theme">Рекомендовано нами!</div>' +
                                                    '<p class="card-title position-absolute dark-theme">' + obj['title'] + '</p>' + 
                                                    '<div class="bottom-img-gradient w-100 position-absolute dark-theme"></div>' +
                                                    '<a href="https://yandex.ru/maps/?text=Тобольск, ' + obj['address'] + '" target="_blank" class="dark-theme">' +
                                                        '<div class="position-absolute sights__gps-mark d-flex d-flex justify-content-center align-items-center dark-theme">' +
                                                            '<i class="fas fa-map-marker-alt dark-theme"></i>' +
                                                        '</div>' +
                                                    '</a>' +
                                                '</div>' +
                                            '</a>' +
                                        '</div>'
                                    )
                                } else {
                                    $('.all-eat').append(
                                        '<div class="col-12 col-md-4 posts-eat last-post-eat dark-theme" data-postid="' + obj['id'] + '">' + 
                                            '<a href="show-to-eat-' + obj['slug'] + '" class="dark-theme">' + 
                                                '<div class="card mt-5 dark-theme">' + 
                                                    '<img src="../../media/' + obj['image_preview'] + '" class="card-img-top round dark-theme">' + 
                                                    '<p class="card-title position-absolute dark-theme">' + obj['title'] + '</p>' + 
                                                    '<div class="bottom-img-gradient w-100 position-absolute dark-theme"></div>' +
                                                    '<a href="https://yandex.ru/maps/?text=Тобольск, ' + obj['address'] + '" target="_blank" class="dark-theme">' +
                                                        '<div class="position-absolute sights__gps-mark d-flex d-flex justify-content-center align-items-center dark-theme">' +
                                                            '<i class="fas fa-map-marker-alt dark-theme"></i>' +
                                                        '</div>' +
                                                    '</a>' +
                                                '</div>' +
                                            '</a>' +
                                        '</div>'
                                    )                                    
                                }
                            } else {
                                if (obj['recomended']) {
                                    $('.all-eat').append(
                                        '<div class="col-12 col-md-4 posts-eat dark-theme">' + 
                                            '<a href="show-to-eat-' + obj['slug'] + '" class="dark-theme">' + 
                                                '<div class="card mt-5 dark-theme">' + 
                                                    '<img src="../../media/' + obj['image_preview'] + '" class="card-img-top round dark-theme">' + 
                                                    '<div class="rec-card dark-theme">Рекомендовано нами!</div>' +
                                                    '<p class="card-title position-absolute dark-theme">' + obj['title'] + '</p>' + 
                                                    '<div class="bottom-img-gradient w-100 position-absolute dark-theme"></div>' +
                                                    '<a href="https://yandex.ru/maps/?text=Тобольск, ' + obj['address'] + '" target="_blank" class="dark-theme">' +
                                                        '<div class="position-absolute sights__gps-mark d-flex d-flex justify-content-center align-items-center dark-theme">' +
                                                            '<i class="fas fa-map-marker-alt dark-theme"></i>' +
                                                        '</div>' +
                                                    '</a>' +
                                                '</div>' +
                                            '</a>' +
                                        '</div>'
                                    )
                                } else {
                                    $('.all-eat').append(
                                        '<div class="col-12 col-md-4 posts-eat dark-theme">' + 
                                            '<a href="show-to-eat-' + obj['slug'] + '" class="dark-theme">' + 
                                                '<div class="card mt-5 dark-theme">' + 
                                                    '<img src="../../media/' + obj['image_preview'] + '" class="card-img-top round dark-theme">' + 
                                                    '<p class="card-title position-absolute dark-theme">' + obj['title'] + '</p>' + 
                                                    '<div class="bottom-img-gradient w-100 position-absolute dark-theme"></div>' +
                                                    '<a href="https://yandex.ru/maps/?text=Тобольск, ' + obj['address'] + '" target="_blank" class="dark-theme">' +
                                                        '<div class="position-absolute sights__gps-mark d-flex d-flex justify-content-center align-items-center dark-theme">' +
                                                            '<i class="fas fa-map-marker-alt dark-theme"></i>' +
                                                        '</div>' +
                                                    '</a>' +
                                                '</div>' +
                                            '</a>' +
                                        '</div>'
                                    )  
                                }
                            }
                        })
                    } else {
                        $.each(res, function(key, obj) {
                            if (obj['last-post-eat']) {
                                if (obj['recomended']) {
                                    $('.all-eat').append(
                                        '<div class="col-12 col-md-4 posts-eat last-post-eat" data-postid="0" data-postidrec="' + obj['id'] + '">' + 
                                            '<a href="show-to-eat-' + obj['slug'] + '">' + 
                                                '<div class="card mt-5">' + 
                                                    '<img src="../../media/' + obj['image_preview'] + '" class="card-img-top round">' + 
                                                    '<div class="rec-card">Рекомендовано нами!</div>' +
                                                    '<p class="card-title position-absolute">' + obj['title'] + '</p>' + 
                                                    '<div class="bottom-img-gradient w-100 position-absolute"></div>' +
                                                    '<a href="https://yandex.ru/maps/?text=Тобольск, ' + obj['address'] + '" target="_blank">' +
                                                        '<div class="position-absolute sights__gps-mark d-flex d-flex justify-content-center align-items-center">' +
                                                            '<i class="fas fa-map-marker-alt"></i>' +
                                                        '</div>' +
                                                    '</a>' +
                                                '</div>' +
                                            '</a>' +
                                        '</div>'
                                    )
                                } else {
                                    $('.all-eat').append(
                                        '<div class="col-12 col-md-4 posts-eat last-post-eat" data-postid="' + obj['id'] + '">' + 
                                            '<a href="show-to-eat-' + obj['slug'] + '">' + 
                                                '<div class="card mt-5">' + 
                                                    '<img src="../../media/' + obj['image_preview'] + '" class="card-img-top round">' + 
                                                    '<p class="card-title position-absolute">' + obj['title'] + '</p>' + 
                                                    '<div class="bottom-img-gradient w-100 position-absolute"></div>' +
                                                    '<a href="https://yandex.ru/maps/?text=Тобольск, ' + obj['address'] + '" target="_blank">' +
                                                        '<div class="position-absolute sights__gps-mark d-flex d-flex justify-content-center align-items-center">' +
                                                            '<i class="fas fa-map-marker-alt"></i>' +
                                                        '</div>' +
                                                    '</a>' +
                                                '</div>' +
                                            '</a>' +
                                        '</div>'
                                    )
                                }
                            } else {
                                if (obj['recomended']) {
                                    $('.all-eat').append(
                                        '<div class="col-12 col-md-4 posts-eat">' + 
                                        '<a href="show-to-eat-' + obj['slug'] + '">' + 
                                            '<div class="card mt-5">' + 
                                                '<img src="../../media/' + obj['image_preview'] + '" class="card-img-top round">' + 
                                                '<div class="rec-card">Рекомендовано нами!</div>' + 
                                                '<p class="card-title position-absolute">' + obj['title'] + '</p>' + 
                                                '<div class="bottom-img-gradient w-100 position-absolute"></div>' +
                                                '<a href="https://yandex.ru/maps/?text=Тобольск, ' + obj['address'] + '" target="_blank">' +
                                                    '<div class="position-absolute sights__gps-mark d-flex d-flex justify-content-center align-items-center">' +
                                                        '<i class="fas fa-map-marker-alt"></i>' +
                                                    '</div>' +
                                                '</a>' +
                                            '</div>' +
                                        '</a>' +
                                        '</div>'
                                    )
                                } else {
                                    $('.all-eat').append(
                                        '<div class="col-12 col-md-4 posts-eat">' + 
                                        '<a href="show-to-eat-' + obj['slug'] + '">' + 
                                            '<div class="card mt-5">' + 
                                                '<img src="../../media/' + obj['image_preview'] + '" class="card-img-top round">' + 
                                                '<p class="card-title position-absolute">' + obj['title'] + '</p>' + 
                                                '<div class="bottom-img-gradient w-100 position-absolute"></div>' +
                                                '<a href="https://yandex.ru/maps/?text=Тобольск, ' + obj['address'] + '" target="_blank">' +
                                                    '<div class="position-absolute sights__gps-mark d-flex d-flex justify-content-center align-items-center">' +
                                                        '<i class="fas fa-map-marker-alt"></i>' +
                                                    '</div>' +
                                                '</a>' +
                                            '</div>' +
                                        '</a>' +
                                        '</div>'
                                    )  
                                }
                            }
                        })
                    }
                }
            }
        })
    })
})
