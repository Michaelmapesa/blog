# from app import create_app



# app = create_app()


# if __name__ == '__main__':
#     app.run()


from multiprocessing import managers
from app import create_app,db
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager, Server
from app.models import User, Blog, Comment 

app = create_app()
manager=Manager(app)
migrate = Migrate(app, db)

manager.add_command('db',MigrateCommand)
@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Blog = Blog, Comment=Comment)

manager.add_command('server',Server)
if __name__ == '__main__':
    manager.run()
