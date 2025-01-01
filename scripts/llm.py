from ollama import generate, GenerateResponse

def get_response(prompt):
  """Helper, use ollama API to return a generated response"""
  response: GenerateResponse = generate(model='llama3.2:3b', prompt=prompt, options={"temperature": 1}).response
  return response