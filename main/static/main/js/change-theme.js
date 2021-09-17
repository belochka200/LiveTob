$(document).ready(function() {
	let theme = '';
	if (localStorage.getItem('theme') == null) {
		theme = 'light'; // по умолчанию будет светлая тема
		localStorage.setItem('theme', theme);
		$('.btn__change-theme').text('Тёмная тема');
	} else theme = localStorage.getItem('theme');

	if (theme == 'light') {
		$('.btn__change-theme').text('Тёмная тема');
	} else {
		$('.btn__change-theme').text('Светлая тема');
		$('*').addClass('dark-theme');
	}

	$('.btn__change-theme').click(function() {
		if (theme == 'light') {
			$('.btn__change-theme').text('Светлая тема');
			theme = 'dark';
			localStorage.setItem('theme', theme);
		} else {
			$('.btn__change-theme').text('Тёмная тема');
			theme = 'light';
			localStorage.setItem('theme', theme);
		}
		$('*').toggleClass('dark-theme');
	});
});
