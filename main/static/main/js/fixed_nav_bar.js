$(document).ready(function(){
    $(window).scroll(function(){
        let top = $(document).scrollTop();
        if(top < 100)  $('nav').css({position: 'relative'});
        else $('nav').css({position: 'fixed', top: '0'});
    });
});