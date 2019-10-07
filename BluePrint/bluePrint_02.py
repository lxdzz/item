from flask import Blueprint

simple_2=Blueprint("simple_page2",__name__)

@simple_2.route("/02/")
def index():
    return "hello world 02"