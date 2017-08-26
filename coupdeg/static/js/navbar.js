$(document).ready(function(){       
	var scroll_start = 0;
	var startchange = $('#startchange');
	var offset = startchange.offset();
	 if (startchange.length){
	$(document).scroll(function() { 
		 scroll_start = $(this).scrollTop();
		 if(scroll_start > offset.top) {
				$("#nav-landing").addClass('navbar-color-slide');			
				$("#nav-landing").removeClass('navbar-color-head');
			} else {
				$("#nav-landing").removeClass('navbar-color-slide');			
				$("#nav-landing").addClass('navbar-color-head');
			}
	});
	 }
});