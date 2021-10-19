$(document).ready(function() {
	let theme = '';
	if (localStorage.getItem('theme') == null) {
		theme = 'light'; // по умолчанию будет светлая тема
		localStorage.setItem('theme', theme);
		$('.theme-toggle').removeClass('fa-sun');
		$('.theme-toggle').addClass('fa-moon');
		$('#logopicture').attr('src', "../../../static/main/img/logo_icon.svg")
	} else theme = localStorage.getItem('theme');

	if (theme == 'light') {
		$('.theme-toggle').removeClass('fa-sun');
		$('.theme-toggle').addClass('fa-moon');
		$('#logopicture').attr('src', "../../../static/main/img/logo_icon.svg")
	} else {
		$('.theme-toggle').removeClass('fa-moon');
		$('.theme-toggle').addClass('fa-sun');
		$('*').addClass('dark-theme');
		$('#logopicture').attr('src', "../../../static/main/img/logo-dark.png")
	}

	$('.btn__change-theme').click(function() {
		if (theme == 'light') {
			$('.theme-toggle').removeClass('fa-moon');
			$('.theme-toggle').addClass('fa-sun');
			theme = 'dark';
			localStorage.setItem('theme', theme);
			$('#logopicture').attr('src', "../../../static/main/img/logo-dark.png")
		} else {
			$('.theme-toggle').removeClass('fa-sun');
			$('.theme-toggle').addClass('fa-moon');
			theme = 'light';
			localStorage.setItem('theme', theme);
			$('#logopicture').attr('src', "../../../static/main/img/logo_icon.svg")
		}
		$('*').toggleClass('dark-theme');
	});
});
