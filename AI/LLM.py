#from llama_cpp import Llama
#
#class LLM:
#	def __init__(self):
#		self.__model = Llama("models/llama-2-7b.Q2_K.gguf", n_ctx=2**15, top_p=0.001)
#
#	def set_lyrics(self, lyrics):
#		self.__lyrics = lyrics
#
#	def generate(self):
#		if self.__lyrics is None:
#			raise ValueError("Can not produce output without lyrics")
#		if self.__model is not None:
#			response = self.__model(f"Make this song goofy/n{self.__lyrics}")
#			return response["choices"][0]["text"]

import openai

class LLM:
    def __init__(self, lyrics: str):
        self.__lyrics = lyrics
        openai.api_key = "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"

    def generate(self):
        response = openai.Completion.create(model="gpt-3.5-turbo-instruct",
            prompt=f"Create a goofy remix of these lyrics: {self.__lyrics}", max_tokens=512)
        return response["choices"][0]["text"]

