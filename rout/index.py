from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from model.model_sport import Sport
from shema.shema_sport import SportShema
from flask_apispec import use_kwargs, marshal_with
from Form.update import EditForm
from Form.date_all import ShowForm

index_route = Blueprint('index', __name__)


@index_route.route('/')
#гланый роутер, который рендерит главную страницу сайта
def get_all():
    return render_template("index.html",
                           title='Home',
                           sports=Sport.get_sport_all())


@index_route.route('/add_sport', methods=['POST'])
#роутер для добавления записи в базу данных(данные из модального окна)
@use_kwargs(SportShema)
def add_sport():
    kwargs = request.form.to_dict()
    add_sports = Sport(**kwargs)
    add_sports.add()
    return redirect("/")


@index_route.route('/delete_sport/<int:id_sport>/', methods=['GET'])
#Функция для удалению записи
def delete_sport(id_sport):
    print(id_sport)
    guid = Sport.get(id_sport)
    guid.delete()
    return redirect("/")


@index_route.route('/update/<int:id_sport>/', methods=['POST'])
#Функция для обновления записи
@use_kwargs(SportShema)
def update_sport(id_sport):
    kwargs = request.form.to_dict()
    update_date = Sport.get(id_sport)
    update_date.update(**kwargs)
    return redirect("/")


@index_route.route('/update/<int:id_sport>/', methods=['GET'])
#переход на страницу обновления
def update_page(id_sport):
    form = EditForm()
    update_date = Sport.get(id_sport)
    form.team.data = update_date.team
    form.name.data = update_date.name
    form.game.data = update_date.game
    form.gold.data = update_date.gold
    form.silver.data = update_date.silver
    form.bronze.data = update_date.bronze
    return render_template("update.html",
                           title='Изменение записи',
                           form=form,
                           id=id_sport)


@index_route.route('/sortup/<date>')
#роутер для сортировки по возврастанию. Производит сортировку данных
# и рендерит страницу с новыми данными
def sort_date_up(date):
    return render_template("index.html",
                           title='Home',
                           sports=Sport.sort(date))


@index_route.route('/sortdown/<date>')
#роутер для сортировки по убыванию. Производит сортировку данных
# и рендерит страницу с новыми данными
def sort_date_down(date):
    return render_template("index.html",
                           title='Home',
                           sports=Sport.sort_down(date))



@index_route.route('/date_for_col/<date>')
#Роутер раститывает min, max, avg и рендерит страницу
# с соответствующими данными
def date_for_col(date):
    forms = ShowForm()
    max = Sport.max_date(date)
    min = Sport.min_date(date)
    avg = Sport.avg_date(date)
    print(avg[0])
    forms.avg_date.data = avg[0]
    forms.min_date.data = min[0]
    forms.max_date.data = max[0]
    return render_template("showDate.html",
                           title='Значения столбца',
                           form=forms)


@index_route.route('/fa/add_sport', methods=['POST'])
#Роутер для демонстрации работы api
# возвращает код запроса, добавляет запись
# в БД по json
@use_kwargs(SportShema)
def fa_add_sport(**kwargs):
    """
    put endpoint
    ---
    consumes:
      - "application/json"
    produces:
      - "application/json"
    tags:
      - Ввод значений в БД
    parameters:
      - in: "body"
        name: "body"
        description: "Значения для вставки в БД"
        required: "true"
        schema:
            type: "object"
            properties:
              order:
                type: "object"
            example: {"name": "test", "team": "test","game": 4, "gold": 3, "silver": 2, "bronze": 1}
    responses:
      500:
        description: Ошибка
      200:
        description: Добавлено в БД
    """
    add_sports = Sport(**kwargs)
    add_sports.add()
    return 'succes', 200


@index_route.route('/avg')
#Роутер для демонстрации работы api
# возвращает среднее значение по переданным данным
@use_kwargs(SportShema)
def avg_date():
    """
    Вывод срезднего в столбце
    ---
    consumes:
      - "application/json"
    produces:
      - "application/json"
    tags:
      - Вывод значений по столбцам
    parameters:
      - in: "query"
        name: "date"
        type: "string"
        required: "true"
        description: (game. gold. silver. bronze)
        schema:
            properties:
              order:
                type: "string"
            example: game
    responses:
      500:
        description: Ошибка
      200:
        description: Добавлено в БД
    """
    args = request.args
    return Sport.avg_date(args.get('date'))


@index_route.route('/fa/index')
#Роутер для демонстрации работы api
# возвращает json всех записей из таблицы
@marshal_with(SportShema(many=True))
def fa_get_all():
    """
    Получение всех значений
    ---
    consumes:
      - "application/json"
    produces:
      - "application/json"
    tags:
      - Вывод из БД всех значений

    responses:
      500:
        description: Ошибка
      200:
        description: Добавлено в БД
    """
    return Sport.get_sport_all()


@index_route.route('/min')
#Роутер для демонстрации работы api
# возвращает минимальное значение по переданным данным
@use_kwargs(SportShema)
def min_date():
    """
    Вывод минимального значений из столбца
    ---
    consumes:
      - "application/json"
    produces:
      - "application/json"
    tags:
      - Вывод значений по столбцам
    parameters:
      - in: "query"
        name: "date"
        type: "string"
        required: "true"
        description: (game. gold. silver. bronze)
        schema:
            properties:
              order:
                type: "string"
            example: game
    responses:
      500:
        description: Ошибка
      200:
        description: Добавлено в БД
    """
    args = request.args
    return Sport.min_date(args.get('date'))


@index_route.route('/max')
#Роутер для демонстрации работы api
# возвращает максимальное значение по переданным данным
@use_kwargs(SportShema)
def max_date():
    """
    максимальное значение в столбце
    ---
    consumes:
      - "application/json"
    produces:
      - "application/json"
    tags:
      - Вывод значений по столбцам
    parameters:
      - in: "query"
        name: "date"
        type: "string"
        required: "true"
        description: (game. gold. silver. bronze)
        schema:
            properties:
              order:
                type: "string"
            example: game
    responses:
      500:
        description: Ошибка
      200:
        description: Добавлено в БД
    """
    args = request.args
    return Sport.max_date(args.get('date'))