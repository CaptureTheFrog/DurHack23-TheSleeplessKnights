from flask import Blueprint, render_template, flash
from application.forms import PostForm
from application.lyrics_custom_api import get_lyrics

backend_blueprint = Blueprint('backend', __name__, template_folder='templates')


@backend_blueprint.route('/', methods=['GET', 'POST'])
def main():
    form = PostForm()
    if form.validate_on_submit():
        lyrics = get_lyrics(form.artist.data, form.title.data)
        if not lyrics:
            flash('Lyrics not found.')
            return render_template('main/index.html', form=form)
        return render_template('main/view_lyrics.html', title=form.title.data, lyrics=lyrics)

    return render_template('main/index.html', form=form)


@backend_blueprint.route('/about')
def about():
    return render_template('navbar/about.html')


@backend_blueprint.route('/contact')
def contact():
    return render_template('navbar/contact.html')


@backend_blueprint.route('/readme')
def readme():
    return render_template('navbar/readme.html')


# @backend_blueprint.route('/view_lyrics')
# def view_lyrics():
#     return render_template('main/view_lyrics.html')
