import unittest
import os
from app import app, db, Order, Event, Correspondents, Department, BackupData
class TestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join('kurbonov.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_home(self):
        result = self.app.get('/')

    def test_backupdata(self):
        b = BackupData(id='1 резервное копирование', backupdate='23.12.2000')
        db.session.add(b)
        db.session.commit()
        assert b.id=='1 резервное копирование'
        assert b.backupdate == '23.12.2000'

    def test_order(self):
        o = Order(id=='1 Приказ'name_of_order='Приказ', content_of_order='Указ', date_of_order='23.12.2000', responsible_of_order='Курбонов', number_of_order='1 приказ', signature='Iskandar', name_of_correspondents='Искандар')
        db.session.add(o)
        db.session.commit()
        assert o.id=='1 Мероприятие'
        assert o.name_of_order == 'Приказ'
        assert o.content_of_order == 'Указ'
        assert o.date_of_order == '23.12.2000'
        assert o.responsible_of_order=='Курбонов'
        assert o.number_of_order=='1 приказ'
        assert o.signature=='Iskandar'
        assert o.name_of_correspondents=='Искандар'

    def test_event(self):
        e = Event(id='1 Мероприятие', name_of_event='Навруз', date_of_event='21.03.2021', mark_of_complete='не выполнено', name_of_order='Указ')
        db.session.add(e)
        db.session.commit()
        assert d.id=='1 Мероприятие'
        assert e.name_of_event=='Навруз'
        assert e.date_of_event=='21.03.2021'
        assert e.mark_of_complete=='не выполнено'
        assert e.name_of_order=='Указ'
        

    def test_department(self):
        d = Department(id='1 подразделение',name_of_department='Подразделение', adress_of_department='Ташкент', number_of_department='1 подразделение')
        db.session.add(d)
        db.session.commit()
        assert d.id=='1 подразделение'
        assert d.name_of_department=='Подразделение'
        assert d.adress_of_department=='Ташкент'
        assert d.number_of_department=='1 подразделение'

    def test_correspondents(self):
        c = Correspondents(name_of_correspondents='Искандар', birthday='23.12.2000', adress_of_correspondents='Ташкент', position='студент', name_of_department='подразделение')
        db.session.add(c)
        db.session.commit()
        assert c.id=='1 Корреспондент'
        assert c.name_of_correspondents=='Искандар'
        assert c.birthday=='23.12.2000'
        assert c.adress_of_correspondents=='Ташкент'
        assert c.position=='студент'
        assert c.name_of_department=='подразделение'

if __name__ == '__main__':
    unittest.main()
