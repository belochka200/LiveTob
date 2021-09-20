$(document).ready(function() {
    $('.btn__show-more-sights').click(function() {
        let lastSightId = $('.last-sight').attr('data-sightid')
        let category = $('.chosen_category').attr('data-categoryid')
        let data = {
            lastSightId: lastSightId,
            category: category,
        }
        $('.sights').removeClass('last-sight')
        $('.sights').removeAttr('data-sightid')
        let url = $('.btn__show-more-sights').attr('btn-url')
        $.ajax({
            method: "GET",
            dataType: "json",
            url: url,
            data: data,
            success: function(data) {
                let result = data['data']
                if (!result) {
                    $('.btn__show-more-sights').fadeOut('slow')
                    $('.no-more').css('display', 'none')
                    $('.no-more').text('Нам нечего показать')
                    $('.no-more').delay(1000).fadeIn('slow')
                    $('.no-more').append('<br><i class="far fa-frown"></i>')
                } else {
                    if ($('body').hasClass('dark-theme')) {
                        $.each(result, function(key, obj) {
                            if (obj['last_sight']) {
                                $('.allsights').append(
                                    '<div class="col-12 col-md-4 sights last-sight dark-theme" data-sightid="' + obj['id'] + '">' + 
                                        '<a href="show-sight-' + obj['slug'] + '" class="url__show-sights dark-theme">' + 
                                            '<div class="card mt-5 dark-theme">' + 
                                                '<img src="../media/' + obj['image_preview'] + '" class="card-img-top round dark-theme">' + 
                                                '<p class="card-title position-absolute dark-theme">' + obj['title'] + '</p>' + 
                                                '<div class="bottom-img-gradient w-100 position-absolute dark-theme"></div>' + 
                                                '<a href="https://yandex.ru/maps/?text=Тобольск, ' + obj['address'] + '" target="_blank">' +
                                                    '<div class="position-absolute sights__gps-mark d-flex d-flex justify-content-center align-items-center dark-theme">' + 
                                                        '<i class="fas fa-map-marker-alt dark-theme"></i>' +
                                                    '</div>' +
                                               ' </a>' +
                                            '</div>' +
                                        '</a>' +
                                    '</div>'
                                )
                            } else {
                                $('.allsights').append(
                                    '<div class="col-12 col-md-4 sights dark-theme">' + 
                                        '<a href="show-sight-' + obj['slug'] + '" class="url__show-sights dark-theme">' + 
                                            '<div class="card mt-5 dark-theme">' + 
                                                '<img src="../media/' + obj['image_preview'] + '" class="card-img-top round dark-theme">' + 
                                                '<p class="card-title position-absolute dark-theme">' + obj['title'] + '</p>' +  
                                                '<div class="bottom-img-gradient w-100 position-absolute dark-theme"></div>' + 
                                                '<a href="https://yandex.ru/maps/?text=Тобольск, ' + obj['address'] + '" target="_blank">' +
                                                    '<div class="position-absolute sights__gps-mark d-flex d-flex justify-content-center align-items-center dark-theme">' + 
                                                        '<i class="fas fa-map-marker-alt dark-theme"></i>' +
                                                    '</div>' +
                                               ' </a>' +
                                            '</div>' +
                                        '</a>' +
                                    '</div>'
                                )
                            }
                        })
                    } else {
                        $.each(result, function(key, obj) {
                            if (obj['last_sight']) {
                                $('.allsights').append(
                                    '<div class="col-12 col-md-4 sights last-sight" data-sightid="' + obj['id'] + '">' + 
                                        '<a href="show-sight-' + obj['slug'] + '" class="url__show-sights">' + 
                                            '<div class="card mt-5">' + 
                                                '<img src="../media/' + obj['image_preview'] + '" class="card-img-top round">' + 
                                                '<p class="card-title position-absolute">' + obj['title'] + '</p>' + 
                                                '<div class="bottom-img-gradient w-100 position-absolute"></div>' + 
                                                '<a href="https://yandex.ru/maps/?text=Тобольск, ' + obj['address'] + '" target="_blank">' +
                                                    '<div class="position-absolute sights__gps-mark d-flex d-flex justify-content-center align-items-center">' + 
                                                        '<i class="fas fa-map-marker-alt"></i>' +
                                                    '</div>' +
                                               ' </a>' +
                                            '</div>' +
                                        '</a>' +
                                    '</div>'
                                )
                            } else {
                                $('.allsights').append(
                                    '<div class="col-12 col-md-4 sights">' + 
                                        '<a href="show-sight-' + obj['slug'] + '" class="url__show-sights">' + 
                                            '<div class="card mt-5">' + 
                                                '<img src="../media/' + obj['image_preview'] + '" class="card-img-top round">' + 
                                                '<p class="card-title position-absolute">' + obj['title'] + '</p>' +  
                                                '<div class="bottom-img-gradient w-100 position-absolute"></div>' + 
                                                '<a href="https://yandex.ru/maps/?text=Тобольск, ' + obj['address'] + '" target="_blank">' +
                                                    '<div class="position-absolute sights__gps-mark d-flex d-flex justify-content-center align-items-center">' + 
                                                        '<i class="fas fa-map-marker-alt"></i>' +
                                                    '</div>' +
                                               ' </a>' +
                                            '</div>' +
                                        '</a>' +
                                    '</div>'
                                )
                            }
                        })
                    }
                }
            }
        })
    })
})
