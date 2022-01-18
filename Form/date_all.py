from flask_wtf import Form
from wtforms import StringField


class ShowForm(Form):
    #Класс для отрисовки формы по выводу данных
    avg_date = StringField('avg_date')
    min_date = StringField('min_date')
    max_date = StringField('max_date')

