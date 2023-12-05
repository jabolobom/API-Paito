from sitePy import app, database, bcrypt
from flask import render_template, url_for, redirect
from sitePy.forms import form_login, form_newaccount
from sitePy.models import Usuarios, foto
from flask_login import login_required, login_user, logout_user, current_user

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/pagetwo", methods=["GET", "POST"])
def pagetwo():
    login = form_login()
    if login.validate_on_submit():
        usuario = Usuarios.query.filter_by(username=login.username.data).first()
        if usuario and bcrypt.check_password_hash(usuario.passw, login.passw.data):
            login_user(usuario)
            return redirect(url_for("after", nome=usuario.username))


    return render_template("pagetwo.html", form=login)

@app.route("/newaccount", methods=["GET", "POST"])
def newaccount():
    new = form_newaccount()
    if new.validate_on_submit():

        senha = bcrypt.generate_password_hash(new.passw.data)
        usuario = Usuarios(username=new.username.data, passw=senha)

        database.session.add(usuario)
        database.session.commit()
        login_user(usuario)

        return redirect(url_for("after", nome=usuario.username))
    else: print(new.errors)

    return render_template("newaccount.html", form=new)

@app.route("/after/<nome>")
@login_required
def after(nome):
    return render_template("after.html", nome=nome)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

