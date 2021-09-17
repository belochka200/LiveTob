$(document).ready(function() {
    let url = document.location.href;
    $('.filter__item').each(function() {
        if(url == (this.href)) {
            $(this).addClass('active');
        }
    });
});