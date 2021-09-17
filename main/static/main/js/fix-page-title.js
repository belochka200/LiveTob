$(document).ready(function() {
	$(window).scroll(function() {
		let top = $(document).scrollTop();
		if (top < 100) {
			$('.page-title').css({position: 'relative'});
		} else {
			$('.page-title').css({position: 'fixed', top: '0'});
		}
	});
});