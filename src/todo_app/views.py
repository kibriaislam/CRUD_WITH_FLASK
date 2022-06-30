from flask import request
from src import app
from flask import  render_template,redirect, url_for

from .models import db , Todo

@app.route('/' ,methods =["GET",])
def home():

    data = Todo.query.all()

    print(data)


    return render_template('home.html', data = data)


@app.route('/task',methods =["POST","GET"])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        
        todo = Todo(title = title, description = description)
        db.session.add(todo)
        db.session.commit()
        
        return redirect(url_for('home'))


@app.route('/delete/<int:id>')
def delete(id):
    data = Todo.query.filter_by(id = id).first()
    db.session.delete(data)
    db.session.commit()
    return redirect('/')

