from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.elements import Null
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'postgresql://itmo:itmo@localhost/itmo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Members(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    contact = db.Column(db.String)
    experience = db.Column(db.String)
    description = db.Column(db.String)

    def __repr__(self):
        return '<Members %r>' % self.id


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    status = db.Column(db.String)
    description = db.Column(db.String)
    date_start = db.Column(db.Date)
    date_end  = db.Column(db.Date)
    link = db.Column(db.String)

    def __repr__(self):
        return '<Projects %r>' % self.id


class Events(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    date_start = db.Column(db.Date)
    date_end  = db.Column(db.Date)
    link = db.Column(db.String)

    def __repr__(self):
        return '<Events %r>' % self.id


@app.route('/members', methods = ['POST'])
def set_member():
    jsonvalues = request.json
    member = Members(name=jsonvalues['name'], surname=jsonvalues['surname'], contact=jsonvalues['contact'], experience=jsonvalues['experience'], description=jsonvalues['description'])
    try:
        db.session.add(member)
        db.session.commit()
        return 'success'
    except:
        return 'error'


@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    values = Members.query.get_or_404(id)
    return jsonify({
        'name': values.name,
        'surname': values.surname,
        'contact': values.contact,
        'experience': values.experience,
        'description': values.description
    })


@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    values = Members.query.get_or_404(id)
    newvalues = request.json
    values.name = newvalues['name']
    values.surname = newvalues['surname']
    values.contact = newvalues['contact']
    values.experience = newvalues['experience']
    values.description = newvalues['description']
    try:
        db.session.commit()
        return 'success'
    except:
        return 'error'


@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    values = Members.query.get_or_404(id)
    try:
        db.session.delete(values)
        db.session.commit()
        return 'success'
    except:
        return 'error'
    

@app.route('/members/count')
def get_members():
    val = Members.query.count()
    return jsonify({
        'count': val
    })


@app.route('/projects', methods = ['POST'])
def set_project():
    jsonvalues = request.json
    project = Projects(name=jsonvalues['name'], status=jsonvalues['status'], description=jsonvalues['description'], date_start=datetime.fromisoformat(jsonvalues['date_start']).date(), date_end=datetime.fromisoformat(jsonvalues['date_end']).date() ,link=jsonvalues['link'])
    db.session.add(project)
    db.session.commit()
    return 'success'

@app.route('/projects/<int:id>', methods=['GET'])
def get_project(id):
    values = Projects.query.get_or_404(id)
    return jsonify({
        'name': values.name,
        'status': values.status,
        'description': values.description,
        'date_start': values.date_start,
        'date_end': values.date_end,
        'link': values.link
    })


@app.route('/projects/<int:id>', methods=['PUT'])
def update_project(id):
    values = Projects.query.get_or_404(id)
    newvalues = request.json
    values.name = newvalues['name']
    values.status = newvalues['status']
    values.description = newvalues['description']
    values.date_start = newvalues['date_start']
    values.date_end = newvalues['date_end']
    values.link = newvalues['link']
    try:
        db.session.commit()
        return 'success'
    except:
        return 'error'


@app.route('/projects/<int:id>', methods=['DELETE'])
def delete_project(id):
    values = Projects.query.get_or_404(id)
    try:
        db.session.delete(values)
        db.session.commit()
        return 'success'
    except:
        return 'error'


@app.route('/projects/count')
def get_projects():
    val = Projects.query.count()
    return jsonify({
        'count': val
    })


@app.route('/events', methods = ['POST'])
def set_event():
    jsonvalues = request.json
    event = Events(name=jsonvalues['name'], description=jsonvalues['description'], date_start=datetime.fromisoformat(jsonvalues['date_start']).date(), date_end=datetime.fromisoformat(jsonvalues['date_end']).date() ,link=jsonvalues['link'])
    db.session.add(event)
    db.session.commit()
    return 'success'


@app.route('/events/<int:id>', methods=['GET'])
def get_event(id):
    values = Events.query.get_or_404(id)
    return jsonify({
        'name': values.name,
        'description': values.description,
        'date_start': values.date_start,
        'date_end': values.date_end,
        'link': values.link
    })


@app.route('/events/<int:id>', methods=['PUT'])
def update_event(id):
    values = Events.query.get_or_404(id)
    newvalues = request.json
    values.name = newvalues['name']
    values.description = newvalues['description']
    values.date_start = newvalues['date_start']
    values.date_end = newvalues['date_end']
    values.link = newvalues['link']
    try:
        db.session.commit()
        return 'success'
    except:
        return 'error'


@app.route('/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    values = Events.query.get_or_404(id)
    try:
        db.session.delete(values)
        db.session.commit()
        return 'success'
    except:
        return 'error'


@app.route('/events/count')
def get_events():
    val = Events.query.count()
    return jsonify({
        'count': val
    })


if __name__ == "__main__":
    app.run(debug=True)