from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Length, NumberRange


class EditForm(Form):
    # Класс для отрисовки формы по обновлению данных
    team = StringField('team', validators=[InputRequired()])
    name = StringField('name', validators=[InputRequired()])
    game = StringField('game', validators=[InputRequired(), NumberRange(min=0, max=140)])
    gold = StringField('gold', validators=[InputRequired(), NumberRange(min=0, max=140)])
    silver = StringField('silver', validators=[InputRequired(), NumberRange(min=0, max=140)])
    bronze = StringField('bronze', validators=[NumberRange(min=0, max=140)])
