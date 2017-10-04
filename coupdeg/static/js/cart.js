$(document).ready( ()=> {       
	$('.add-to-cart').on('click', function(event){
		event.preventDefault();
		$('.add-to-cart-pop').addClass('is-visible');
	});
	
	//close popup
	$('.add-to-cart-pop').on('click', function(event){
		if( $(event.target).is('.cd-popup-close') || $(event.target).is('.add-to-cart-pop') || $(event.target).is('.cd-popup-no') ) {
			event.preventDefault();
			$(this).removeClass('is-visible');
		}
		if( $(event.target).is('.cd-popup-yes') ) {
			console.log($(".cd-popup-yes input").val())
			$.ajax({
				url: '/user/history',
				data : {'product_id': $(".add-to-cart-pop .cd-popup-yes input").val() },
			});
			event.preventDefault();
			$(this).removeClass('is-visible');
		}
	});
});