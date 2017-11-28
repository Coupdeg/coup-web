$(document).ready( ()=> {       
	var inp = document.getElementById('image-upload');
	inp.addEventListener('change', function(e){
			var file = this.files[0];
			var reader = new FileReader();
			reader.onload = function(){
					document.getElementById('product-image').src = this.result;
					};
			reader.readAsDataURL(file);
			},false);
});