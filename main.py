from src.flask_server.run_server import app
from src.flask_server.context_db import run_db

if __name__ == '__main__':
    run_db()
    app.run(debug=True)