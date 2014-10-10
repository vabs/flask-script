
$(function(){

	// get listings + reviews
	setInterval(function(){
				getData('Listings');
				getData('Reviews')}, 
			5000);

});


function getData (url_name) {
	$.get('get' + url_name, function(data){
		if( url_name == 'Listings') {
			updateListings(data);
		}
		else{
			updateReviews(data);
		}
	});
}

function updateListings(listings) {
	for(var ls in listings['listings']) {
		var item = listings['listings'][ls];
		$("#listing").append("<p>" + item['token_id'] + " " + item['listing_name']);
	}
}

function updateReviews(reviews) {
	for(var ls in reviews['reviews']) {
		var item = reviews['reviews'][ls];
		$("#reviews").append("<p>" + item['token_id'] + " " + item['review_source']);
	}

}
