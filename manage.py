from flask.ext.script import Manager
from main import app

manager = Manager(app)

@manager.command
@manager.option('-h', '--hello', help="Say Hello!")
def hello(hello='vabs'):
    print ("hello " + hello)


if __name__ == '__main__':
	manager.run()