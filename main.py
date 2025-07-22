import werkzeug
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")

# LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI", "sqlite:///users.db")
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get('email')

        if User.query.filter_by(email=email).first():
            flash("You've already signed up. Please log in.")
            return redirect(url_for('login'))


        hashed_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8,
        )

        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=hashed_and_salted_password

        )


        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return render_template("secrets.html", name=new_user.name)

    return render_template("register.html")

@login_manager.user_loader
def load_user(id):
    return db.session.get(User, int(id))


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if not user:
            flash("That email does not exist. Please try again or register.")
            return redirect(url_for('login'))

        if not check_password_hash(user.password, password):
            flash("Incorrect password. Please try again.")
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('secrets'))

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    name = request.args.get("name")
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)

