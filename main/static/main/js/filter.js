$(document).ready(function() {
    $('.filter__btn').click(function() {
        $('.filter__btn').toggleClass('active');
        $('.filter__menu').toggleClass('active');
    });
    $('.filter__btn-in-menu').click(function() {
        $('.filter__btn').toggleClass('active');
        $('.filter__menu').toggleClass('active');
    })
});