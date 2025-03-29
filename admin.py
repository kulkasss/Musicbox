from flask import redirect, url_for
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import FileUploadField, Select2Widget
from flask_admin.menu import MenuLink
from flask_login import current_user
from wtforms_sqlalchemy.fields import QuerySelectField

from config import Config
from models import Artist, Song, User, db


# Кастомна головна сторінка адмінки
class MyAdminIndexView(AdminIndexView):
    @expose("/")
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for("login"))
        return super().index()


# Обмежений доступ до адмінки
class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("login"))


class UserAdmin(AdminModelView):
    column_list = ["id", "username"]
    column_labels = {"username": "Логін"}
    can_edit = False  # Вимикаємо можливість редагування
    can_create = False  # Вимикаємо можливість створення нових користувачів
    can_view_details = True  # Дозволяємо перегляд користувача


class ArtistAdmin(AdminModelView):
    column_labels = {"name": "Ім'я"}


# Обираємо категорію для товару
class SongAdmin(AdminModelView):
    column_list = ("artist", "title")
    column_labels = {
        "artist": "Автор",
        "title": "Назва",
    }
    form_columns = ["artist", "title", "file",]
    form_overrides = {"artist": QuerySelectField, "file": FileUploadField}
    form_args = {
        "artist": {
            "query_factory": lambda: Artist.query.all(),
            "get_label": "name",
            "allow_blank": False,
            "widget": Select2Widget(),
        },
        "file": {
            "label": "Пісня",
            "base_path": Config.UPLOAD_FOLDER,
            "allowed_extensions": {"mp3"},
        },
    }


# Створюємо об'єкт адмінки
admin = Admin(
    name="Адмінка ",
    template_mode="bootstrap4",
    index_view=MyAdminIndexView(),
)

admin.add_link(MenuLink(name="🏠 Перейти до Musicbox", url="/"))
admin.add_link(MenuLink(name="🚪 Вийти", url="/logout"))
# Додаємо моделі в адмінку
admin.add_view(ArtistAdmin(Artist, db.session, name="Виконавці"))
admin.add_view(SongAdmin(Song, db.session, name="Пісні"))
admin.add_view(UserAdmin(User, db.session, name="Користувачі"))