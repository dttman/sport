from rout import db
from sqlalchemy import func, text, desc


class Sport(db.Model):
    # Класс для работы с БД
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team = db.Column(db.String(100))
    name = db.Column(db.String(100))
    game = db.Column(db.Integer)
    gold = db.Column(db.Integer)
    silver = db.Column(db.Integer)
    bronze = db.Column(db.Integer)

    def __init__(self, team, name, game, gold, silver, bronze):
        self.team = team
        self.name = name
        self.game = game
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    @classmethod
    #Получение всех значений из БД
    def get_sport_all(cls):
        sports = cls.query.all()
        return sports

    @classmethod
    # Получение конкретной записи по id
    def get(cls, id):
        try:
            sport = cls.query.get(id)
            if not id:
                raise Exception('No api with this id')
        except Exception:
            db.session.rollback()
            raise
        return sport

    # Обновление записи
    def update(self, **kwargs):
        try:
            for key, value in kwargs.items():
                setattr(self, key, value)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise

    #Удаление записи
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise

    #Добавление записи
    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise

    @classmethod
    def sort(cls, what="team"):
        # Сортировка данных по возврастанию
        sort_date = cls.query.order_by(what)
        return sort_date

    @classmethod
    def sort_down(cls, what="team"):
        # Сортировка данных по убыванию
        sort_date = cls.query.order_by(desc(what))
        return sort_date

    @classmethod
    def avg_date(cls, date="gold"):
        # Среднеее значение по столбцу
        sql = text('SELECT AVG('+date+') FROM sport')
        result = db.engine.execute(sql)
        avg = [row[0] for row in result]
        return avg

    @classmethod
    def max_date(cls, date):
        # Получение максимального значения по столбцу
        sql = text('SELECT MAX('+date+') FROM sport')
        result = db.engine.execute(sql)
        max_date = [row[0] for row in result]
        return max_date

    @classmethod
    def min_date(cls, date="gold"):
        # Получение минимального значения по столбцу
        sql = text('SELECT MIN('+date+') FROM sport')
        result = db.engine.execute(sql)
        min_date = [row[0] for row in result]
        return min_date
