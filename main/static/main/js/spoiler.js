$(document).ready(function() {
    $('.spoiler-head').click(function() {
        $(this).parents('.spoiler-wrap').find('.spoiler-body').slideToggle();
        $(this).parents().toggleClass('active');
    })
})