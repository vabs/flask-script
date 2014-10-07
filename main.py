from flask import Flask, jsonify

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello():
	return jsonify({'status': 'ok'})


if __name__ == "__main__":
	app.run()	
