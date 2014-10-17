var g_listings, g_reviews;
$(function(){
	setInterval(function(){
				getData();}, 
			5000);

});


function getData () {
	$.get('getValues', function(data){
		var s_table = $("table#listing");
		s_table.html('');
		s_table.append('<tr><th>Name</th><th>Listings</th><th>Reviews</th></tr>');
		for(var o in data){
			var b = data[o];
			var row = '<tr><td>' + b['name'] + '</td><td>' + b['listing'] + '</td><td>' + b['review'] + '</td></tr>';
			s_table.append(row);
		}
	});
}



