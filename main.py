from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///itmo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Values(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    members = db.Column(db.Integer)
    projects = db.Column(db.Integer)
    events = db.Column(db.Integer)

    def __repr__(self):
        return '<Values %r>' % self.id


@app.route('/')
def index():
    values = Values.query.first()
    return f"Участников: {values.members}\nПроектов: {values.projects}\nСобытий: {values.events}"


@app.route('/update', methods=['POST', 'GET'])
def update():
    values = Values.query.first()
    if request.method == 'POST':
        values.members = request.form['members']
        values.projects = request.form['projects']
        values.events = request.form['events']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Ошибка рекдактирования"
    else:
        return "Редактирование"
if __name__ == "__main__":
    app.run(debug=True)