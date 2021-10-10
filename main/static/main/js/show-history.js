$(document).ready(function() {
    if (localStorage.getItem('show-history')) {
        $('.read-history-block').css('display', 'none');
    }
    $('.btn-no-show-history').click(function() {
        $(".read-history-block").slideUp(800)
        localStorage.setItem('show-history', 'no-show')
    })
    $('.btn-show-history').click(function() {
        localStorage.setItem('show-history', 'show')
    })
})