from . import app
from . import views


app.add_url_rule("/", view_func=views.index)
app.add_url_rule("/position/create", view_func=views.position_create, methods=["GET", "POST"])

app.add_url_rule("/employee/create", view_func=views.employee_create, methods=["GET", "POST"])
app.add_url_rule("/employee/update/<int:id>", view_func=views.employee_update, methods=["GET", "POST"])
app.add_url_rule("/employee/delete/<int:id>", view_func=views.employee_delete, methods=["GET", "POST"])

app.add_url_rule("/register", view_func=views.register, methods=["GET", "POST"])
app.add_url_rule("/login", view_func=views.login, methods=["GET", "POST"])
app.add_url_rule("/logout", view_func=views.logout, methods=["GET"])
