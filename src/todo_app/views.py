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


@app.route('/update/<int:id>' , methods = ['GET','POST'])
def update(id):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        data = Todo.query.filter_by(id = id).first()
        data.title = title
        data.description = description
        db.session.add(data)
        db.session.commit()
        
        return redirect('/')

    data = Todo.query.filter_by(id = id).first()
    return render_template('update.html',todo = data)


def status_update(id):
    if request.method == 'POST':
        status = request.form['status']
        data = Todo.query.filter_by(id = id).first()
        data.status = status
        db.session.add(data)
        db.session.commit()
        
        return redirect('/')

    data = Todo.query.filter_by(id = id).first()
    return render_template('update.html',todo = data)


def Something(id):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        data = Todo.query.filter_by(id = id).first()
        data.title = title
        data.description = description
        db.session.add(data)
        db.session.commit()
        
        return redirect('/')

    data = Todo.query.filter_by(id = id).first()
    return render_template('update.html',todo = data)
