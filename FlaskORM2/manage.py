import os
from app import models,create
from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate

app=create()
manage=Manager(app)
migrate=Migrate(app,models)
app.secret_key="123456"

manage.add_command("db",MigrateCommand)

if __name__=="__main__":
    manage.run()
