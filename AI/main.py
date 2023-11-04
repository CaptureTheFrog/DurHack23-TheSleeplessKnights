from llama_cpp import Llama

class LLM:
	def __init__(self):
		self.__model = Llama("../models/llama-2-7b.Q2_K.gguf")

	def set_lyrics(self, lyrics):
		if self.__model is not None:
			self.__model(lyrics)
