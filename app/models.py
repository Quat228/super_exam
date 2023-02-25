from flask_login import UserMixin
from . import bcrypt, db, login_manager


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    department = db.Column(db.String)
    wage = db.Column(db.Integer)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    inn = db.Column(db.String)
    position_id = db.Column(db.Integer, db.ForeignKey("position.id"))
    position = db.relationship("Position", backref=db.backref("employees", lazy="dynamic"))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, new_password):
        self.password_hash = bcrypt.generate_password_hash(new_password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __str__(self):
        return self.username
