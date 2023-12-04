from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from sitePy.models import user

class form_login(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    passw = PasswordField("password", validators=[DataRequired()])
    confirmButton = SubmitField("login")

class form_newaccount(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    passw = PasswordField("password", validators=[DataRequired()])
    confirmation_passw = PasswordField("password confirmation", validators=[DataRequired(), EqualTo("passw")])
    confirmButton = SubmitField("register")

    def validate_username(self, username):
        tester = user.query.filter_by(username=username.data).first() # Testa se o usuario existe na database
        if tester:
            return ValidationError("Existing user")