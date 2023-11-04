from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')

from application.views import backend_blueprint
app.register_blueprint(backend_blueprint)


if __name__ == '__main__':
    app.run()
