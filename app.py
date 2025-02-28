from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

from models import db, Song, Artist
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS


@app.route("/")
def index():
    Song = Song.query.all()
    return render_template("index.html", song=song)

@app.route("/add", methods=["POST"])
def add_song():
    title = request.form.get("title", "").strip()
    author = request.form.get("a", "").strip()
    file = request.files.getlist("file")
    filename = secure_filename(file.filename)
    if title and file and allowed_file(file.filename):
        new_song = Song(title=title, )
            # На випадок, якщо ми маємо кілька файлів з однаковими іменами
            # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            # name = f"{timestamp}_{name}"

            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])

            file.save(file_path)
            db.session.add(new_file)

        db.session.add(new_song)
        db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    task = Song.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for("index"))

@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get(task_id)
    if task and request.method == "POST":
        task.title = request.form.get("title", "").strip()
        if task.title:
            db.session.commit()
            return redirect(url_for("index"))
    return render_template("edit.html", task=task)


