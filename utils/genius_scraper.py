import requests

class Genius:
    def __init__(self, song_name: str, artist: str) -> None:
        self.webpage = requests.get(f"https://genius.com/{artist.replace(' ', '-')}")