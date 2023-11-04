from AI.LLM import LLM
model = LLM()
model.set_lyrics("how does one calculate the diameter of a donut") # Test prompt to make sure the LLM can understand prompts
print(model.generate())
