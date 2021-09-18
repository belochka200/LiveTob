$(document).ready(function() {
    $('.btn__show-more-rest').click(function() {
        let lastid = $('.last-post-rest').attr('data-postid')
        let category = $('.chosen_category').attr('data-categoryid')
        let data = { 
            lastid: lastid,
            category: category
        }
        $('.posts-rest').removeClass('last-post-rest')
        $('.posts-rest').removeAttr('data-postid')
        let url = $('.btn__show-more-rest').attr('btn-url')
        $.ajax({
            method: "GET",
            dataType: "json",
            url: url,
            data: data,
            success: function(data) {
                let res = data['data']
                if (!res) {
                    $('.btn__show-more-rest').fadeOut('slow')
                    $('.no-more').css('display', 'none')
                    $('.no-more').text('Нам нечего показать')
                    $('.no-more').delay(1000).fadeIn('slow')
                    $('.no-more').append('<br><i class="far fa-frown"></i>')
                } else {
                    if ($('body').hasClass('dark-theme')) {
                        $.each(res, function(key, obj) {
                            if (obj['last-post-rest']) {
                                $('.all-posts-rest').append(
                                    '<div class="col-12 col-md-4 post-rest last-post-rest dark-theme" data-postid="' + obj['id'] + '">' +
                                        '<a href="show-to-rest-' + obj['slug'] + '" class="dark-theme">' +
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
                            } else {
                                $('.all-posts-rest').append(
                                    '<div class="col-12 col-md-4 post-rest dark-theme"">' +
                                        '<a href="show-to-rest-' + obj['slug'] + '" class="dark-theme">' +
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
                        })
                    } else {
                        $.each(res, function(key, obj) {
                            if (obj['last-post-rest']) {
                                $('.all-posts-rest').append(
                                    '<div class="col-12 col-md-4 post-rest last-post-rest" data-postid="' + obj['id'] + '">' +
                                        '<a href="show-to-rest-' + obj['slug'] + '">' +
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
                            } else {
                                $('.all-posts-rest').append(
                                    '<div class="col-12 col-md-4 post-rest">' +
                                        '<a href="show-to-rest-' + obj['slug'] + '">' +
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
                        })
                    }
                }
            }
        })
    })
})
