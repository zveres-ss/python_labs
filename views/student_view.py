from myapp import app
from myapp import db
from student import Student
from flask import jsonify
from student_schema import StudentSchema

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

# endpoint to create new user
@app.route("/students", methods=["POST"])
def add_student():
    first_name = request.json['firstName']
    last_name = request.json['lastName']
    
    new_student = Student()
    new_student.first_name = first_name
    new_student.last_name = last_name

    db.session.add(new_student)
    db.session.commit()

    return jsonify(new_student)


# endpoint to show all users
@app.route("/students", methods=["GET"])
def get_user():
    all_users = Student.query.all()
    result = students_schema.dump(all_users)
    return jsonify(result)


# endpoint to get user detail by id
@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)


# endpoint to update user
@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    user = User.query.get(id)
    username = request.json['username']
    email = request.json['email']

    user.email = email
    user.username = username

    db.session.commit()
    return user_schema.jsonify(user)


# endpoint to delete user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)
