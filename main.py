# from utils.LLM import LLM
# from utils.image_gen import gen_image

from utils.genius_scraper import Genius

obj = Genius("feel good inc", "gorillaz")
print(obj.webpage.text)
# model = LLM()
#gen_image("Cats")