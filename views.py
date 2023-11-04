from flask import render_template, redirect

from app import app
from forms import LyricForm


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = LyricForm()
    if form.validate_on_submit():
        # Do something here

        return redirect('output.html')
    return render_template('index.html', form=form)


