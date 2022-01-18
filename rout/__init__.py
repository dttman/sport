from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flasgger import Swagger
from flask_fontawesome import FontAwesome

#определение папок с хранением шаблонов и стилей
app = Flask(__name__, template_folder='../templates', static_folder='../static')
#Строка подключения к базе данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sport.db'

db = SQLAlchemy(app)
ma = Marshmallow(app)

swagger = Swagger(app)
fa = FontAwesome(app)
#Подключение и регистрация роутов
from rout.index import index_route
app.register_blueprint(index_route)
