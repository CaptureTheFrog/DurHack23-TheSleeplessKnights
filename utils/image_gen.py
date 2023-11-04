import openai
import requests

from keys import openaikey


def gen_image(prompt):
    openai.api_key = openaikey

    generated_data = openai.Image.create(
        prompt=f"{prompt}",
        n=1,
        size="1024x1024",
        response_format="url",
    )

    print(generated_data["data"][0]["url"])

    filename = "static/images/" + prompt[:16] + ".jpg"

    generated_image_data = requests.get(generated_data["data"][0]["url"]).content
    with open(filename, 'wb') as handler:
        handler.write(generated_image_data)


def art_for_song(song_title):
    gen_image(f"Album Art for a song titled '{song_title}'")
