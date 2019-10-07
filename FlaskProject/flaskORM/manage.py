import sys
from models import models
from views import app
from flask_script import Manager
from flask_migrate import MigrateCommand

manage=Manager(app)

# @manage.command
# def migrate():
#     models.create_all()

manage.add_command("db",MigrateCommand)

if __name__=="__main__":
    manage.run()
