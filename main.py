from os import environ
from src.flask_server.run_server import app
from src.flask_server.context_db import run_db

if __name__ == '__main__':
    run_db()
    app.run(host="0.0.0.0", port=10000)