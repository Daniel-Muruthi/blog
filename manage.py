from app import create_app, db
from flask_script import Manager, Server
from app.models import User
from flask_migrate import Migrate, MigrateCommand
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os.path as op
from flask_admin.contrib.fileadmin import FileAdmin

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

admin = Admin(app)
admin.add_view(ModelView(User, db.session))
path = op.join(op.dirname(__file__), 'static')
admin.add_view(FileAdmin(path, './app/static', name='Static Files'))

# Creating a python shell for  testing features in our apps and debugging using flask_script 

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User)


if __name__ == '__main__':
    manager.run()