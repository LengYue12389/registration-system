import warnings
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flaskr import create_app
from flaskr.models import db

warnings.filterwarnings("ignore")
app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()
