$(document).ready(function() {
    if (!$('.chosen_category').text().trim()) {
        $('.chosen_category').css({'display': 'none'});
        $('.content').removeClass('active');
    } else {
        $('.content').addClass('active');
    }
});