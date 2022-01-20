from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flasgger import Swagger
from flask_fontawesome import FontAwesome

#определение папок с хранением шаблонов и стилей
app = Flask(__name__, template_folder='../templates', static_folder='../static')
#Строка подключения к базе данных
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sport.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zqcqxjcwbdpnfi:e1e08e86c3d4e8f4e8a38d28032701fad5788b4e017fdf9af348d48aeb69e532@ec2-52-6-178-202.compute-1.amazonaws.com:5432/d39e2dl6jihnp1'

db = SQLAlchemy(app)
ma = Marshmallow(app)

swagger = Swagger(app)
fa = FontAwesome(app)
#Подключение и регистрация роутов
from rout.index import index_route
app.register_blueprint(index_route)
