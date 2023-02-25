import wtforms as wf

from flask_wtf import FlaskForm
from .models import Position
from . import app


def get_position_choices():
    positions = Position.query.all()
    choices = []
    for position in positions:
        choices.append((position.id, position.name))
    return choices


class PositionForm(FlaskForm):
    name = wf.StringField(label="Название должности", validators=[
        wf.validators.DataRequired()
    ])
    department = wf.StringField(label="Отдел")
    wage = wf.IntegerField(label="Ставка заработной платы", validators=[
        wf.validators.DataRequired()
    ])

    def validate_wage(self, field):
        if field.data < 0:
            raise wf.ValidationError("Число не может быть отрицательным")


class EmployeeForm(FlaskForm):
    name = wf.StringField(label="Имя", validators=[
        wf.validators.DataRequired()
    ])
    inn = wf.StringField(label="ИНН", validators=[
        wf.validators.DataRequired()
    ])
    position_id = wf.SelectField(label="Позиция", validators=[
        wf.validators.DataRequired()
    ], choices=[])

    def validate_inn(self, field):
        if len(field.data) != 14:
            raise wf.ValidationError("В инн должно быть ровно 14 символов")
        if field.data[0] not in ["1", "2"]:
            raise wf.ValidationError("Первое число в инн должно начинаться с 1 или 2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position_id.choices = get_position_choices()


class UserForm(FlaskForm):
    username = wf.StringField(label="Логин")
    password = wf.PasswordField(label="Пароль")
