from app import create_app
from flask_script import Manager, Server


# Creating my app instance

app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

# Creating a python shell for  testing features in our apps and debugging using flask_script

@manager.shell
def make_shell_context():
    return dict(app = app)

if __name__ == '__main__':
    manager.run()