$(document).ready(function() {
    $('.btn__show-more-to-do').click(function() {
        let lastid = $('.last-post-to-do').attr('data-postid')
        let lastrecid = $('.last-post-to-do').attr('data-postidrec')
        let category = $('.chosen_category').attr('data-categoryid')
        let data = { 
            lastid: lastid,
            lastrecid: lastrecid,
            category: category
        }
        $('.posts-to-do').removeClass('last-post-to-do')
        $('.posts-to-do').removeAttr('data-postid')
        $('.posts-to-do').removeAttr('data-postidrec')
        let url = $('.btn__show-more-to-do').attr('btn-url')
        $.ajax({
            method: "GET",
            dataType: "json",
            url: url,
            data: data,
            success: function(data) {
                let result = data['data']
                if (!result) {
                    $('.btn__show-more-to-do').fadeOut('slow')
                    $('.no-more').css('display', 'none')
                    $('.no-more').text('Нам нечего показать')
                    $('.no-more').delay(1000).fadeIn('slow')
                    $('.no-more').append('<br><i class="far fa-frown"></i>')
                } else {
                    if ($('body').hasClass('dark-theme')) {
                        $.each(result, function(key, obj) {
                            if (obj['last-post-to-do']) {
                                if (obj['recomended']) {
                                    $('.all-to-do').append(
                                        '<div class="col-12 col-md-4 posts-to-do last-post-to-do dark-theme" data-postid="0" data-postidrec="' + obj['id'] + '">' + 
                                            '<a href="show-to-do-' + obj['slug'] + '" class="dark-theme">' + 
                                                '<div class="card mt-5 dark-theme">' + 
                                                    '<img src="../../media/' + obj['image_preview'] + '" class="card-img-top round dark-theme">' + 
                                                    '<div class="card-title position-absolute dark-theme">' + 
                                                        '<div class="row align-items-center dark-theme">' +
                                                            '<div class="col-12 col-xl-7 dark-theme">' + obj['title'] + '</div>' + 
                                                            '<div class="col-12 col-xl-5 dark-theme">' + 
                                                                '<div class="rec-card col-12 text-center fw-bold dark-theme">Рекомендуем</div>' + 
                                                                '<div class="col-12 card-category fw-bold dark-theme mt-1">' + obj['category'] + '</div>' +
                                                            '</div>' + 
                                                        '</div>' +
                                                    '</div>' + 
                                                    '<a href="https://yandex.ru/maps/?text=Тобольск, ' + obj['address'] + '" target="_blank">' +
                                                        '<div class="position-absolute sights__gps-mark d-flex d-flex justify-content-center align-items-center dark-theme">' + 
                                                            '<i class="fas fa-map-marker-alt dark-theme"></i>' +
                                                        '</div>' +
                                                    '</a>' +
                                                '</div>' +
                                            '</a>' +
                                        '</div>'
                                    )
                                } else {
                                    $('.all-to-do').append(
                                        '<div class="col-12 col-md-4 posts-to-do last-post-to-do dark-theme" data-postid="' + obj['id'] + '">' + 
                                            '<a href="show-to-do-' + obj['slug'] + '" class="dark-theme">' + 
                                                '<div class="card mt-5 dark-theme">' + 
                                                    '<img src="../../media/' + obj['image_preview'] + '" class="card-img-top round dark-theme">' + 
                                                    '<div class="card-title position-absolute dark-theme">' + 
                                                        '<div class="row align-items-center dark-theme">' +
                                                            '<div class="col-12 col-xl-7 dark-theme">' + obj['title'] + '</div>' + 
                                                            '<div class="col-12 col-xl-5 dark-theme">' + 
                                                                '<div class="col-12 card-category fw-bold dark-theme">' + obj['category'] + '</div>' +
                                                            '</div>' + 
                                                        '</div>' +
                                                    '</div>' + 
                                                    '<a href="https://yandex.ru/maps/?text=Тобольск, ' + obj['address'] + '" target="_blank">' +
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
                                    $('.all-to-do').append(
                                        '<div class="col-12 col-md-4 posts-to-do dark-theme">' + 
                                            '<a href="show-to-do-' + obj['slug'] + '" class="dark-theme">' + 
                                                '<div class="card mt-5 dark-theme">' + 
                                                    '<img src="../../media/' + obj['image_preview'] + '" class="card-img-top round dark-theme">' + 
                                                    '<div class="card-title position-absolute dark-theme">' + 
                                                        '<div class="row align-items-center dark-theme">' +
                                                            '<div class="col-12 col-xl-7 dark-theme">' + obj['title'] + '</div>' + 
                                                            '<div class="col-12 col-xl-5 dark-theme">' + 
                                                                '<div class="rec-card col-12 text-center fw-bold dark-theme">Рекомендуем</div>' + 
                                                                '<div class="col-12 card-category fw-bold dark-theme">' + obj['category'] + '</div>' +
                                                            '</div>' + 
                                                        '</div>' +
                                                    '</div>' + 
                                                    '<a href="https://yandex.ru/maps/?text=Тобольск, ' + obj['address'] + '" target="_blank">' +
                                                        '<div class="position-absolute sights__gps-mark d-flex d-flex justify-content-center align-items-center dark-theme">' + 
                                                            '<i class="fas fa-map-marker-alt dark-theme"></i>' +
                                                        '</div>' +
                                                    '</a>' +
                                                '</div>' +
                                            '</a>' +
                                        '</div>'
                                    )
                                } else {
                                    $('.all-to-do').append(
                                        '<div class="col-12 col-md-4 posts-to-do dark-theme">' + 
                                            '<a href="show-to-do-' + obj['slug'] + '" class="dark-theme">' + 
                                                '<div class="card mt-5 dark-theme">' + 
                                                    '<img src="../../media/' + obj['image_preview'] + '" class="card-img-top round dark-theme">' + 
                                                    '<div class="card-title position-absolute dark-theme">' + 
                                                        '<div class="row align-items-center dark-theme">' +
                                                            '<div class="col-12 col-xl-7 dark-theme">' + obj['title'] + '</div>' + 
                                                            '<div class="col-12 col-xl-5 dark-theme">' + 
                                                                '<div class="col-12 card-category fw-bold dark-theme">' + obj['category'] + '</div>' +
                                                            '</div>' + 
                                                        '</div>' +
                                                    '</div>' + 
                                                    '<a href="https://yandex.ru/maps/?text=Тобольск, ' + obj['address'] + '" target="_blank">' +
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
                        $.each(result, function(key, obj) {
                            if (obj['last-post-to-do']) {
                                if (obj['recomended']) {
                                    $('.all-to-do').append(
                                        '<div class="col-12 col-md-4 posts-to-do last-post-to-do" data-postid="0" data-postidrec="' + obj['id'] + '">' + 
                                            '<a href="show-to-do-' + obj['slug'] + '">' + 
                                                '<div class="card mt-5">' + 
                                                    '<img src="../../media/' + obj['image_preview'] + '" class="card-img-top round">' + 
                                                    '<div class="card-title position-absolute">' + 
                                                        '<div class="row align-items-center">' +
                                                            '<div class="col-12 col-xl-7">' + obj['title'] + '</div>' + 
                                                            '<div class="col-12 col-xl-5">' + 
                                                                '<div class="rec-card col-12 text-center fw-bold">Рекомендуем</div>' + 
                                                                '<div class="col-12 card-category fw-bold">' + obj['category'] + '</div>' +
                                                            '</div>' + 
                                                        '</div>' +
                                                    '</div>' + 
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
                                    $('.all-to-do').append(
                                        '<div class="col-12 col-md-4 posts-to-do last-post-to-do" data-postid="' + obj['id'] + '">' + 
                                            '<a href="show-to-do-' + obj['slug'] + '">' + 
                                                '<div class="card mt-5">' + 
                                                    '<img src="../../media/' + obj['image_preview'] + '" class="card-img-top round">' + 
                                                    '<div class="card-title position-absolute">' + 
                                                        '<div class="row align-items-center">' +
                                                            '<div class="col-12 col-xl-7">' + obj['title'] + '</div>' + 
                                                            '<div class="col-12 col-xl-5">' + 
                                                                '<div class="col-12 card-category fw-bold">' + obj['category'] + '</div>' +
                                                            '</div>' + 
                                                        '</div>' +
                                                    '</div>' + 
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
                                    $('.all-to-do').append(
                                        '<div class="col-12 col-md-4 posts-to-do">' + 
                                            '<a href="show-to-do-' + obj['slug'] + '">' + 
                                                '<div class="card mt-5">' + 
                                                    '<img src="../../media/' + obj['image_preview'] + '" class="card-img-top round">' + 
                                                    '<div class="card-title position-absolute">' + 
                                                        '<div class="row align-items-center">' +
                                                            '<div class="col-12 col-xl-7">' + obj['title'] + '</div>' + 
                                                            '<div class="col-12 col-xl-5">' + 
                                                                '<div class="rec-card col-12 text-center fw-bold">Рекомендуем</div>' + 
                                                                '<div class="col-12 card-category fw-bold">' + obj['category'] + '</div>' +
                                                            '</div>' + 
                                                        '</div>' +
                                                    '</div>' + 
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
                                    $('.all-to-do').append(
                                        '<div class="col-12 col-md-4 posts-to-do">' + 
                                            '<a href="show-to-do-' + obj['slug'] + '">' + 
                                                '<div class="card mt-5">' + 
                                                    '<img src="../../media/' + obj['image_preview'] + '" class="card-img-top round">' + 
                                                    '<div class="card-title position-absolute">' + 
                                                        '<div class="row align-items-center">' +
                                                            '<div class="col-12 col-xl-7">' + obj['title'] + '</div>' + 
                                                            '<div class="col-12 col-xl-5">' + 
                                                                '<div class="col-12 card-category fw-bold">' + obj['category'] + '</div>' +
                                                            '</div>' + 
                                                        '</div>' +
                                                    '</div>' + 
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