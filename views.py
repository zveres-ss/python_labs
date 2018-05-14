from myapp import app
from models import Member
from student import Student

@app.route('/')
def index():
    #firstmember = Member.query.first()
    return '<h1>The first member is </h1>'

@app.route('/view')
def view():
    student = Student.query.first()
    return 'member name' + student.first_name
