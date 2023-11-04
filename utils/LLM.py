import openai

from keys import openaikey


class LLM:
    def __init__(self, lyrics: str):
        self.__lyrics = lyrics
        openai.api_key = openaikey

    def generate(self):
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f"Compose a humorous first-person narrative as if you are the lyrics of {self.__lyrics}, providing a whimsical tale of the song's content, including a comical exploration of its verses, pre-chorus, chorus, and any humorous elements within the lyrics.",
            max_tokens=512
        )
        return response["choices"][0]["text"]
