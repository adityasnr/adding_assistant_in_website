from html.entities import name2codepoint
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from assistant import Assistant


# For Todo Administration Page 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tasks.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable= False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
    
@app.route('/', methods = ['GET','POST'] )
def dashboard():
    return render_template("dashboard.html")

@app.route('/assistant', methods = ['GET','POST'] )
def assistant():
    Assistant.start('self')
    if request.method == 'POST':
        answer = request.form['search']
    Assistant.one(answer = answer)
    return render_template("assistant.html")

@app.route('/add-task', methods = ['GET','POST'] )
def AddTasks():
    if request.method == "POST":
       title = request.form['title']
       desc = request.form['desc']
       todo = Todo(title=title, desc=desc)
       db.session.add(todo)
       db.session.commit()
    allTodo = Todo.query.all()
    return render_template("add-task.html", allTodo = allTodo)


# To update Todo
@app.route("/update/<int:sno>" , methods = ['GET', 'POST'])
def update(sno):
    if request.method == "POST":
       title = request.form['title']
       desc = request.form['desc']
       todo = Todo.query.filter_by(sno=sno).first()
       todo.title = title
       todo.desc = desc
       db.session.add(todo)
       db.session.commit()
       return redirect("/add-task")
    todo = Todo.query.filter_by(sno = sno).first()
    return render_template("update.html", todo = todo)
   

# To delete Todo
@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/add-task")


# For people and users

@app.route('/show')
def home8():  
    if request.method == "POST":
       title = request.form['title']
       desc = request.form['desc']
       todo = Todo(title=title, desc=desc)
       db.session.add(todo)
       db.session.commit()
    allTodo = Todo.query.all()
    return render_template("show.html",allTodo = allTodo )



if __name__ == '__main__':
    app.run(debug = True, port = 4000)


















