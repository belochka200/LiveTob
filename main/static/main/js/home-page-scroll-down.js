$(document).ready(function() {
    $('.home-page__scroll-down').click(function() {
        $('html, body').animate({
            scrollTop: $('#home-page-screen-city-history').offset().top
        }, 250, "linear")
    })
})