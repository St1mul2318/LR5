from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kurbonov.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class BackupData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    backupdate = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<BackupData %r>' % self.id


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_order = db.Column(db.String(100), nullable=False)
    date_of_order = db.Column(db.Integer, nullable=False)
    content_of_order = db.Column(db.String(100), nullable=False)
    responsible_of_order = db.Column(db.String(100), nullable=False)
    number_of_order = db.Column(db.Integer, nullable=False)
    signature = db.Column(db.String(100), nullable=False)
    name_of_correspondents = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Order %r>' % self.id


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_event = db.Column(db.String(100), nullable=False)
    date_of_event = db.Column(db.Integer, nullable=False)
    mark_of_complete = db.Column(db.String(100), nullable=False)
    name_of_order = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return '<Event %r>' % self.id


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_department = db.Column(db.String(100), nullable=False)
    adress_of_department = db.Column(db.String(100), nullable=False)
    number_of_department = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Department %r>' % self.id


class Correspondents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_correspondents = db.Column(db.String(100), nullable=False)
    birthday = db.Column(db.Integer, nullable=False)
    adress_of_correspondents = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    name_of_department = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Correspondents %r>' % self.id


@app.route('/backup')
def backup():
    backup = BackupData.query.order_by(BackupData.id.desc()).all()
    return render_template("backup.html", backup=backup)


@app.route('/backup/<int:id>/update', methods=['POST', 'GET'])
def backup_update(id):
    backup = BackupData.query.get(id)
    if request.method == "POST":
        backup.backupdate = request.form['backupdate']

        try:
            db.session.commit()
            return redirect('/backup')
        except:
            return "При радактировании резервных данных произошла ошибка"
    else:
        return render_template("update_backup.html", backup=backup)


@app.route('/create_backup', methods=['GET', 'POST'])
def backup_create():
    if request.method == "POST":
        backupdate = request.form['backupdate']

        backup = BackupData(backupdate=backupdate)

        try:
            db.session.add(backup)
            db.session.commit()
            return redirect('/backup')
        except:
            return "При добавлении резервных данных произошла ошибка"
    else:
        return render_template("create_backup.html")


@app.route('/backup/<int:id>/delete')
def backup_delete(id):
    backup = BackupData.query.get_or_404(id)

    try:
        db.session.delete(backup)
        db.session.commit()
        return redirect('/backup')
    except:
        return "При удалении приказа произошла ошибка"


@app.route('/backup/<int:id>')
def backup_detail(id):
    backup = BackupData.query.get(id)
    return render_template("backup_detail.html", backup=backup)


@app.route('/order')
def order():
    order = Order.query.order_by(Order.id.desc()).all()
    return render_template("order.html", order=order)


@app.route('/order/<int:id>/update', methods=['POST', 'GET'])
def order_update(id):
    order = Order.query.get(id)
    if request.method == "POST":
        order.name_of_order = request.form['name_of_order']
        order.date_of_order = request.form['date_of_order']
        order.content_of_order = request.form['content_of_order']
        order.responsible_of_order = request.form['responsible_of_order']
        order.number_of_order = request.form['number_of_order']
        order.signature = request.form['signature']
        order.name_of_correspondents = request.form['name_of_correspondents']

        try:
            db.session.commit()
            return redirect('/order')
        except:
            return "При радактировании приказа произошла ошибка"
    else:
        return render_template("update_order.html", order=order)


@app.route('/create_order', methods=['GET', 'POST'])
def order_create():
    if request.method == "POST":
        name_of_order = request.form['name_of_order']
        date_of_order = request.form['date_of_order']
        content_of_order = request.form['content_of_order']
        responsible_of_order = request.form['responsible_of_order']
        number_of_order = request.form['number_of_order']
        signature = request.form['signature']
        name_of_correspondents = request.form['name_of_correspondents']

        order = Order(name_of_order=name_of_order, date_of_order=date_of_order, content_of_order=content_of_order, responsible_of_order=responsible_of_order,
        number_of_order=number_of_order, signature=signature, name_of_correspondents=name_of_correspondents)

        try:
            db.session.add(order)
            db.session.commit()
            return redirect('/order')
        except:
            return "При добавлении приказа произошла ошибка"
    else:
        return render_template("create_order.html")


@app.route('/order/<int:id>/delete')
def order_delete(id):
    order = Order.query.get_or_404(id)

    try:
        db.session.delete(order)
        db.session.commit()
        return redirect('/order')
    except:
        return "При удалении приказа произошла ошибка"


@app.route('/order/<int:id>')
def order_detail(id):
    order = Order.query.get(id)
    return render_template("order_detail.html", order=order)


@app.route('/event')
def event():
    event = Event.query.order_by(Event.id.desc()).all()
    return render_template("event.html", event=event)


@app.route('/event/<int:id>/delete')
def event_delete(id):
    event = Event.query.get_or_404(id)

    try:
        db.session.delete(event)
        db.session.commit()
        return redirect('/event')
    except:
        return "При удалении мероприятия произошла ошибка"


@app.route('/event/<int:id>/update', methods=['POST', 'GET'])
def event_update(id):
    event = Event.query.get(id)
    if request.method == "POST":
        event.name_of_event = request.form['name_of_event']
        event.date_of_event = request.form['date_of_event']
        event.mark_of_complete = request.form['mark_of_complete']
        event.name_of_order = request.form['name_of_order']

        try:
            db.session.commit()
            return redirect('/event')
        except:
            return "При радактировании мероприятия произошла ошибка"
    else:
        return render_template("update_event.html", event=event)


@app.route('/create_event', methods=['POST', 'GET'])
def event_create():
    if request.method == "POST":
        name_of_event = request.form['name_of_event']
        date_of_event = request.form['date_of_event']
        mark_of_complete = request.form['mark_of_complete']
        name_of_order = request.form['name_of_order']

        event = Event(name_of_event=name_of_event, date_of_event=date_of_event, 
        mark_of_complete=mark_of_complete, name_of_order=name_of_order)

        try:
            db.session.add(event)
            db.session.commit()
            return redirect('/event')
        except:
            return "При добавлении мероприятия произошла ошибка"
    else:
        return render_template("create_event.html")


@app.route('/event/<int:id>')
def event_detail(id):
    event = Event.query.get(id)
    return render_template("event_detail.html", event=event)


@app.route('/department')
def department():
    department = Department.query.order_by(Department.id.desc()).all()
    return render_template("department.html", department=department)


@app.route('/department/<int:id>')
def department_detail(id):
    department = Department.query.get(id)
    return render_template("department_detail.html", department=department)


@app.route('/department/<int:id>/delete')
def department_delete(id):
    department = Department.query.get_or_404(id)

    try:
        db.session.delete(department)
        db.session.commit()
        return redirect('/department')
    except:
        return "При удалении подразделения произошла ошибка"


@app.route('/department/<int:id>/update', methods=['POST', 'GET'])
def department_update(id):
    department = Department.query.get(id)
    if request.method == "POST":
        #departme
        department.name_of_department = request.form['name_of_department']
        department.adress_of_department = request.form['adress_of_department']
        department.number_of_department = request.form['number_of_department']

        try:
            db.session.commit()
            return redirect('/department')
        except:
            return "При радактировании подразделения произошла ошибка"
    else:
        return render_template("update_department.html", department=department)


@app.route('/create_department', methods=['GET', 'POST'])
def department_create():
    if request.method == "POST":

        name_of_department = request.form['name_of_department']
        adress_of_department = request.form['adress_of_department']
        number_of_department = request.form['number_of_department']

        department = Department(name_of_department=name_of_department, adress_of_department=adress_of_department, number_of_department=number_of_department)

        try:
            db.session.add(department)
            db.session.commit()
            return redirect('/department')
        except:
            return "При добавлении подразделения произошла ошибка"
    else:
        return render_template("create_department.html")


@app.route('/correspondents')
def correspondents():
    correspondents = Correspondents.query.order_by(Correspondents.id.desc()).all()
    return render_template("correspondents.html", correspondents=correspondents)


@app.route('/correspondents/<int:id>')
def correspondents_detail(id):
    correspondents = Correspondents.query.get(id)
    return render_template("correspondents_detail.html", correspondents=correspondents)


@app.route('/correspondents/<int:id>/delete')
def correspondents_delete(id):
    correspondents = Correspondents.query.get_or_404(id)

    try:
        db.session.delete(correspondents)
        db.session.commit()
        return redirect('/correspondents')
    except:
        return "При удалении корреспондента произошла ошибка"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/correspondents/<int:id>/update', methods=['POST', 'GET'])
def correspondents_update(id):
    correspondents = Correspondents.query.get(id)
    if request.method == "POST":
        #corresponden
        correspondents.name_of_correspondents = request.form['name_of_correspondents']
        correspondents.birthday = request.form['birthday']
        correspondents.adress_of_correspondents = request.form['adress_of_correspondents']
        correspondents.position = request.form['position']
        correspondents.name_of_department = request.form['name_of_department']

        try:
            db.session.commit()
            return redirect('/correspondents')
        except:
            return "При радактировании корреспондента произошла ошибка"
    else:
        return render_template("update_correspondents.html", correspondents=correspondents)


@app.route('/create_correspondents', methods=['GET', 'POST'])
def correspondents_create():
    if request.method == "POST":

        name_of_correspondents = request.form['name_of_correspondents']
        birthday = request.form['birthday']
        adress_of_correspondents = request.form['adress_of_correspondents']
        position = request.form['position']
        name_of_department = request.form['name_of_department']

        correspondents = Correspondents(name_of_correspondents=name_of_correspondents, birthday=birthday,
         adress_of_correspondents=adress_of_correspondents, position=position, name_of_department=name_of_department)

        try:
            db.session.add(correspondents)
            db.session.commit()
            return redirect('/correspondents')
        except:
            return "При добавлении корреспондента произошла ошибка"
    else:
        return render_template("create_correspondents.html")


if __name__ == "__main__":
    app.run(debug=True)