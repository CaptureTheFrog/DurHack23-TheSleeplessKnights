# load the large language model file
from llama_cpp import Llama
LLM = Llama("models/llama-2-7b.Q2_K.gguf")

# create a text prompt
prompt = "Say Hello World"
# generate a response (takes several seconds)
output = LLM(prompt)

# display the response
print(output["choices"][0]["text"])
