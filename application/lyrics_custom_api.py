import requests
import re


class Scraper:
    def __init__(self, song_name: str, artist: str) -> None:
        link = f"https://www.songlyrics.com/{self.replace_spaces(artist.lower())}/{self.replace_spaces(song_name.lower())}-lyrics/"
        self.webpage = requests.get(link)
        self.data = re.findall(r"^([a-zA-Z \.\,\!\?\;\:\'\"\(\)\[\]\{\}\-]*?)<br \/>", self.webpage.text, re.MULTILINE)
        self.lyrics = "\n".join(self.data)

    def replace_spaces(self, string):
        return string.replace(" ", "-")