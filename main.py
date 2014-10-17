from flask import Flask, jsonify, request, render_template
import json
import traceback
import sys

app = Flask(__name__)
app.debug = True

#vars used for page
global listings
global reviews
global tokens

@app.route('/')
def hello():
	global tokens
	try:
		tokens
	except NameError:
		print ("well, it WASN'T defined after all!")
		tokens = {}

	return render_template('home.html', tokens=tokens)


@app.route('/updatetoken', methods=['POST'])
def udpate_token():
	try:
		print('update tokens')
		global tokens
		try:
			tokens
		except NameError:
			print ("define for the first time!!")
			tokens = {}

		raw_str = request.get_data().decode('utf-8')
		json_obj = json.loads(raw_str)
		tokens[json_obj['token']] = {'listing': 0, 'review': 0, 'name': json_obj['location_name']}
		print('created token for location: ', json_obj['location_name'])
		return jsonify({'status': 'ok'})
	except:
		print('error saving tokens')
		return jsonify({'status': 'fail'})



@app.route('/updatevalues', methods=['POST'])
def update_value():
	global tokens
	print('updating values')
	raw_str = request.get_data().decode('utf-8')
	json_obj = json.loads(raw_str)
	print(json_obj)

	try:
		if json_obj['listing']:
			print('listing maybe ', json_obj['listing'])
			tokens[json_obj['token']]['listing'] += 1
			print('done udpating listing')
	except KeyError:
		try:
			if json_obj['review']:
				print('listing maybe ', json_obj['review'])
				tokens[json_obj['token']]['review'] += 1
				print('done udpating reviews')
		except KeyError:
			print ('not proper request')
			print(json_obj)

	return jsonify({'status': 'ok'})


@app.route('/getValues')
def get_values():
	global tokens
	try:
		tokens
	except NameError:
		print ("define for the first time!!")
		tokens = {}
		traceback.print_exc(file=sys.stdout)
	return jsonify(**tokens)


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
