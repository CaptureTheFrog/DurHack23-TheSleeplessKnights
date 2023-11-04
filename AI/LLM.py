from llama_cpp import Llama

class LLM:
	def __init__(self):
		self.__model = Llama("models/llama-2-7b.Q2_K.gguf")

	def set_lyrics(self, lyrics):
		self.__lyrics = lyrics

	def generate(self):
		if self.__model is not None:
			response = self.__model(self.__lyrics)
			return response["choices"][0]["text"]
