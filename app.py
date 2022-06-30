from src import app
from src.todo_app.models import db


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port = 8000)