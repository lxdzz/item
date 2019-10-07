from flask import Flask
from bluePrint_01 import simple_1
from bluePrint_02 import simple_2

app=Flask(__name__)
app.register_blueprint(simple_1)
app.register_blueprint(simple_2)
app.run()
