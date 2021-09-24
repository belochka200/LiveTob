$(document).ready(function() {
    if (localStorage.getItem('alert-popular-people') != null) {
        $('.alert-popular-people').css('display', 'none');
    } else {
        $('.alert-popular-people-btn').click(function() {
            $('.alert-popular-people').slideUp(800);
            localStorage.setItem('alert-popular-people', 'true')
        })
    }
})