from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

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


@app.route('/members/get')
def get_members():
    values = Values.query.first()
    return str(values.members)


@app.route('/members/set', methods=['POST'])
def set_members():
    values = Values.query.first()
    values.members = request.form['count']
    try:
        db.session.commit()
        return "success"
    except:
        return "error"


@app.route('/projects/get')
def get_projects():
    values = Values.query.first()
    return str(values.projects)


@app.route('/projects/set', methods=['POST'])
def set_projects():
    values = Values.query.first()
    values.projects = request.form['count']
    try:
        db.session.commit()
        return "success"
    except:
        return "error"


@app.route('/events/get')
def get_events():
    values = Values.query.first()
    return str(values.events)


@app.route('/events/set', methods=['POST'])
def set_events():
    values = Values.query.first()
    values.events = request.form['count']
    try:
        db.session.commit()
        return "success"
    except:
        return "error"


if __name__ == "__main__":
    app.run(debug=True)