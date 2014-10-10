from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
app.debug = True

#vars used for page
val = 10

@app.route('/')
def hello():
	return render_template('home.html', value = val)


@app.route('/listing', methods=['POST'])
def show_listings():
	return jsonify({'status': 'ok'})


@app.route('/in', methods=['GET'])
def increment():
	val += 1
	return jsonify({'status': 'ok'})	

if __name__ == "__main__":
	app.run()	
