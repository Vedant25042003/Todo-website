from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///toDo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ToDo(db.Model):
    Sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

# used to print
    def __repr__(self) -> str:
        return f"{self.Sno} - {self.title}"

with app.app_context():
    db.create_all()  # Wrap in app context
    print("Database initialized.")

# app routr gives endpoint for multiple pages website 
# means that pericular route will route to a perticulqr page of website
@app.route('/', methods = ['GET', 'POST'])
def newtodo():
    if request.method == 'POST':
        # print(request.form['title']) 
        title = request.form['title']
        desc = request.form['desc']
        todo = ToDo(title = title, desc =desc)
        db.session.add(todo)
        db.session.commit()
    alltodo = ToDo.query.all()
    # print(alltodo)
    return render_template('index.html', alltodo=alltodo)


@app.route('/update/<int:Sno>', methods = ['GET', 'POST'])
def update(Sno):
    if request.method == 'POST':
        # print(request.form['title']) 
        title = request.form['title']
        desc = request.form['desc']
        todo = ToDo.query.filter_by(Sno=Sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    todo = ToDo.query.filter_by(Sno=Sno).first()
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:Sno>')
def delete(Sno):
    alltodo = ToDo.query.filter_by(Sno=Sno).first()
    db.session.delete(alltodo)
    db.session.commit()
    return redirect("/")

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)

