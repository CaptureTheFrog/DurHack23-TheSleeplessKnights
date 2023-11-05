from flask import Blueprint, render_template, flash, send_file
from application.forms import PostForm
from application.lyrics_custom_api import Scraper
from utils.LLM import LLM
from utils.image_gen import art_for_song
from utils.tts_gen import text_to_speech, play_audio
from utils.lyric_fetcher import get_lyrics
import os


backend_blueprint = Blueprint('backend', __name__, template_folder='templates')


@backend_blueprint.route('/<filename>')
def serve_audio(filename):
    return send_file(filename)

@backend_blueprint.route('/', methods=['GET', 'POST'])
def main():
    form = PostForm()
    if form.validate_on_submit():
        scraper = Scraper(form.title.data, form.artist.data)
        lyrics = scraper.lyrics or get_lyrics(form.artist.data, form.title.data)
        if not lyrics:
            flash('Lyrics not found.')
            return render_template('main/index.html', form=form)
        else:
            new_lyrics = LLM(lyrics).generate()
            art_for_song(form.title.data)
            speech_file = text_to_speech(new_lyrics)
        path = "/static/images/" + form.title.data + ".jpg"
        return render_template('main/view_lyrics.html', title=form.title.data, path=path, lyrics=new_lyrics)

    return render_template('main/index.html', form=form)


@backend_blueprint.route('/about')
def about():
    return render_template('navbar/about.html')


@backend_blueprint.route('/contact')
def contact():
    return render_template('navbar/contact.html')


@backend_blueprint.route('/readme')
def readme():
    f = open('README.md')
    md = f.read()
    f.close()
    return render_template('navbar/readme.html',readme=md)



@backend_blueprint.route('/button_clicked', methods=['GET', 'POST'])
def button_clicked():
    # Perform some action when the button is clicked
    print("Button was clicked!")
    play_audio('speech.mp3')
