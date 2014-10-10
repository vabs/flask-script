from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)
app.debug = True

#vars used for page
global listings
global reviews

@app.route('/')
def hello():
	global listings
	global reviews
	try:
		listings
	except NameError:
		print ("well, it WASN'T defined after all!")
		listings = {}

	try:
		reviews
	except NameError:
		print ("well, it WASN'T defined after all!")
		reviews = {}

	return render_template('home.html', listings = listings, reviews=reviews)


@app.route('/listings', methods=['GET', 'POST'])
def listings_fill():
	print('listings incoming')
	raw_str = request.get_data().decode('utf-8')
	json_obj = json.loads(raw_str)
	global listings
	try:
		listings
	except NameError:
		print ("well, it WASN'T defined after all!")
		listings = []
		listings.append(json_obj)
		return jsonify({'status': 'fail'})
	else:
		print ("sure, it was defined.")
		listings.append(json_obj)
	return jsonify({'status': 'ok'})


@app.route('/reviews', methods=['GET', 'POST'])
def reviews_fill():
	print('reviews incoming')
	raw_str = request.get_data().decode('utf-8')
	json_obj = json.loads(raw_str)
	global reviews
	try:
		reviews
	except NameError:
		print ("well, it WASN'T defined after all!")
		reviews = []
		reviews.append(json_obj)
		return jsonify({'status': 'first time'})
	else:
		print ("sure, it was defined.")
		reviews.append(json_obj)
	return jsonify({'status': 'ok'})


@app.route('/getListings')
def getlisting():
	global listings
	return jsonify({'listings': listings})


@app.route('/getReviews')
def getreviews():
	global reviews
	return jsonify({'reviews': reviews})


@app.errorhandler(404)
def handle_404(e):
	return jsonify({'status': '404'})	


@app.errorhandler(500)
def handle_500(e):
	return jsonify({'status': '500'})	

if __name__ == "__main__":
	app.run()	
