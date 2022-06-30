from telnetlib import STATUS
from turtle import title
from src import app
from flask_sqlalchemy import SQLAlchemy

import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = "asfjf888sffsfsdfsfnothinggksadkasdj"
app.config[' SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class Todo(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(256),nullable = False)
    description = db.Column(db.Text)
    status = db.Column(db.Boolean,default = False)
    created_at =  db.Column(db.DateTime, nullable=False,default=datetime.datetime.now())


    def __repr__(self) -> str:
        return f"Taks: {self.title},status:{self.status}"