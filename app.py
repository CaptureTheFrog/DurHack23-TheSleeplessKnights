from flask import Flask, render_template

from forms import LyricForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "LongAndRandomSecretKey"


@app.route('/')
def index():  # put application's code here
    form = LyricForm()
    return render_template("index.html", form=form)


if __name__ == '__main__':
    app.run()
