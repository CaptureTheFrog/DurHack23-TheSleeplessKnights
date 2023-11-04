from llama_cpp import Llama
PROMPT = "Rewrite the lyrics to the following song in the most verboose and convoluted way imaginable. You must always refer in the first person as if you are the song. The lyrics must be in the language the song was originally written in. You must rewrite the entire song"

class LLM:
	def __init__(self):
		self.__model = Llama("models/llama-2-7b.Q2_K.gguf", n_ctx=4096, last_n_tokens_size=4096)

	def set_lyrics(self, lyrics):
		self.__lyrics = lyrics

	def generate(self):
		if self.__model is not None:
			response = self.__model(f"{PROMPT}: {self.__lyrics}")
			return response["choices"][0]["text"]
