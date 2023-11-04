import base64

import requests

from keys import img_key


def gen_image(prompt):
    url = ("https://api.getimg.ai/v1/stable-diffusion/text-to-image")

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {img_key}"
    }

    generation_data = {
        "prompt": f"{prompt}",
        "output_format": "jpeg",
        "width": 1024,
        "height": 1024
    }

    response = requests.post(url, headers=headers, json=generation_data)

    print(response.text)

    generated_data = response.json()

    generated_image_data = base64.b64decode(generated_data['image'])

    with open('art/generated_image.jpeg', 'wb') as f:
        f.write(generated_image_data)


def art_for_song(song_title):
    gen_image(f"Album Art for a song titled '{song_title}'")
