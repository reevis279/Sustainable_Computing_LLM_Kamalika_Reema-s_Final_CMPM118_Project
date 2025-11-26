
#First make sure to run this code within a virtual environment
#Ask user to input promt for ollama model
print("Give me a prompt and I'll tell you how much power ollama takes to answer it.")
prompt = input("Enter your prompt: ")
#print("This is prompt:", prompt)

#Get this application to check if ollama is installed.

#If ollama isn't install then tell user to install ollama.

#If ollama is installed, ask it the prompt.
import ollama #error here, even though I have ollama installed

response = ollama.chat(model='mistral', messages=[
  {
    'role': 'user',
    'content': prompt,
  },
])
print(response['message']['content'])
