from flask import Flask, jsonify, request, render_template
import json
import traceback
import sys
import datetime

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
		tokens[json_obj['token']] = {'listing': 0, 'review': 0, 'name': json_obj['location_name'], 'start_time': datetime.datetime.now(), 'last_updated_at': datetime.datetime.now()}
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
			tokens[json_obj['token']]['last_updated_at'] = datetime.datetime.now()
			print('done udpating listing')
	except KeyError:
		try:
			if json_obj['review']:
				print('review maybe ', json_obj['review'])
				tokens[json_obj['token']]['review'] += 1
				tokens[json_obj['token']]['last_updated_at'] = datetime.datetime.now()
				print('done udpating reviews')
		except KeyError:
			print ('not proper request')
			print(json_obj)
			tokens[json_obj['token']] = {'listing': 0, 'review': 0, 'name': json_obj['location_name'], 'start_time': datetime.datetime.now(), 'last_updated_at': datetime.datetime.now()}
		

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


@app.errorhandler(404)
def handle_404(e):
	return jsonify({'status': '404'})	


@app.errorhandler(500)
def handle_500(e):
	return jsonify({'status': '500'})	

if __name__ == "__main__":
	app.run()	
