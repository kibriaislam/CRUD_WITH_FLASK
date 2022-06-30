from flask import Flask

app = Flask(__name__ ,template_folder='todo_app/templates')

from src.todo_app import views 