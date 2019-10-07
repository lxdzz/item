from flask import Blueprint

simple_1=Blueprint("simple_page1",__name__)

@simple_1.route("/01/")
def index():
    return "hello world 01"

