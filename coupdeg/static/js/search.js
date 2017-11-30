$(document).ready(function(){       
	// $("")
	$("#search-input").hide();
	$("#search-button").on("click",function() {
		$("#login").fadeOut();
		$("#cart").fadeOut();
		$('#search-button').fadeOut(function () {
			$('#search-input').animate({
				width: "toggle"
			});
	});
	});
	$("#close-search").on("click", function() {
		$('#search-input').animate({
			width: "toggle"
		}, function() {
			$("#login").fadeIn();
			$("#cart").fadeIn();
			$('#search-button').fadeIn();
		});
	});
});	