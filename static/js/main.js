var g_listings, g_reviews;
$(function(){
	setInterval(function(){
				// getData();
				updateCount();
			}, 
			5000);
});


function getData () {
	$.get('getValues', function(data){
		var s_table = $("table#listing");
		s_table.html('');
		s_table.append('<tr><th>Name</th><th>Listings</th><th>Reviews</th><th>Started At</th><th>Last Updated At</th></tr>');
		for(var o in data){
			var b = data[o];
			var row = '<tr><td>' + b['name'] + '</td><td>' + b['listing'] + '</td><td>' + b['review'] + 
					'</td><td>' + b['start_time'] + '</td><td>' + b['last_updated_at'] + '</td></tr>';
			s_table.append(row);
		}
	});
}

function updateCount(){
	$.get('getRL', function(data){
		//$("#listingCount")
	});
}


function saveData(){
	$.get('savetodb', function(data){
		console.log(data);
	});
}
