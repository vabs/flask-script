from flask.ext.script import Manager
from flask import Flask, jsonify

app = Flask(__name__)
app.debug = True

manager = Manager(app)
manager.run()

@manager.command
@manager.option('-h', '--hello', help="Say Hello!")
def hello(hello='vabs'):
    print ("hello " + hello)

@app.route('/')
def hello():
	return jsonify({'status': 'ok'})


if __name__ == "__main__":
	app.run()	