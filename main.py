from AI.LLM import LLM
model = LLM()
model.set_lyrics("These are song lyrics")
print(model.generate())
