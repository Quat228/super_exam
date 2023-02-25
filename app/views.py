from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required,logout_user
from . import db, models, forms


def index():
    employees = models.Employee.query.all()
    return render_template("index.html", employees=employees)


def position_create():
    form = forms.PositionForm()
    if request.method == "POST":
        if form.validate_on_submit():
            position = models.Position()
            form.populate_obj(position)
            db.session.add(position)
            db.session.commit()
            flash("Должность успешно сохранена", category="success")
        else:
            print(form.errors)
    return render_template("standard_form.html", form=form)


def employee_create():
    form = forms.EmployeeForm()
    if request.method == "POST":
        if form.validate_on_submit():
            employee = models.Employee()
            form.populate_obj(employee)
            db.session.add(employee)
            db.session.commit()
            flash("Сотрудник успешно сохранен", category="success")
            return redirect(url_for("index"))
        else:
            print(form.errors)
    return render_template("standard_form.html", form=form)


def employee_update(id):
    employee = models.Employee.query.get(id)
    form = forms.EmployeeForm(obj=employee)
    if request.method == "POST":
        if form.validate_on_submit():
            form.populate_obj(employee)
            db.session.add(employee)
            db.session.commit()
            flash("Сотрудник успешно сохранен", category="success")
            return redirect(url_for("index"))
        else:
            print(form.errors)
    return render_template("standard_form.html", form=form)


def employee_delete(id):
    employee = models.Employee.query.get(id)
    if request.method == "POST":
        db.session.delete(employee)
        db.session.commit()
        flash("Сотрудник успешно удален", category="success")
        return redirect(url_for("index"))
    return render_template("confirm_delete.html", employee=employee)


def register():
    title = "Регистрация"
    form = forms.UserForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = models.User()
            form.populate_obj(user)
            db.session.add(user)
            db.session.commit()
            flash("Пользователь успешно сохранен", category="success")
            return redirect(url_for("login"))
        else:
            print(form.errors)
    return render_template("user_form.html", form=form, title=title)


def login():
    title = "Авторизация"
    form = forms.UserForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = models.User.query.filter_by(username=form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                return redirect(url_for("index"))
            else:
                print("Неправильные данные")
        else:
            print(form.errors)
    return render_template("user_form.html", form=form, title=title)


def logout():
    logout_user()
    return redirect(url_for("login"))


