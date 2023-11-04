from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')

from application.views import backend_blueprint
app.register_blueprint(backend_blueprint)

@app.errorhandler(400)
def bad_request(error):
    return render_template("errors/400.html"), 400


@app.errorhandler(403)
def access_denied(error):
    return render_template("errors/403.html"), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template("errors/500.html"), 500


@app.errorhandler(503)
def service_unavailable(error):
    return render_template("errors/503.html"), 503

if __name__ == '__main__':
    app.run()
