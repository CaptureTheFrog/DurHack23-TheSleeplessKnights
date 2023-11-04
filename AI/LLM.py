from llama_cpp import Llama

class LLM:
	def __init__(self):
		self.__model = Llama("models/llama-2-7b.Q2_K.gguf", n_ctx=2**15, n_gqa=8)

	def set_lyrics(self, lyrics):
		self.__lyrics = lyrics

	def generate(self):
		if self.__model is not None:
			response = self.__model(f"Compose a humorous first-person narrative as if you are the following lyrics: [{self.__lyrics}] providing a whimsical tale of the song's content, including a comical exploration of its verses, pre-chorus, chorus, and any humorous elements within the lyrics. Ensure to keep the language the same as the original lyrics")
			return response["choices"][0]["text"]
