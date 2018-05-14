from myapp import db

class Student(db.Model):
    __tablename__ = 'students'
    student_id = db.Column('id', db.Integer, primary_key = True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
