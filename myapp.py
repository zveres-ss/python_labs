from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from views import *
import sys
sys.path.insert(0, 'views')

#import student_view

from views.student_view import *

if __name__ == '__main__':
    app.run()
