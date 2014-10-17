var g_listings, g_reviews;
$(function(){
	setInterval(function(){
				getData();}, 
			5000);

});


function getData () {
	$.get('getValues', function(data){
		console.log(data);
	});
}



