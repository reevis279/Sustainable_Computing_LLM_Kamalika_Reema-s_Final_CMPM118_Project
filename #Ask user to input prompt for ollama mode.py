
#First make sure to run this code within a virtual environment
#Ask user to input promt for ollama model
print("Give me a prompt and I'll tell you how much power ollama takes to answer it.")
prompt = input("Enter your prompt: ")
#print("This is prompt:", prompt)

#Get this application to check if ollama is installed.
#Probably have to use subprocess to run a command line instruction to check if ollama is installed.


#If ollama isn't install then tell user to install ollama.
#Probably have to use a config file to install ollama
#Probably have to use docker to use config file

#run quen 2.5-coder 3b model in lmstudio config file here

#If ollama is installed, ask it the prompt.
import ollama #error here, even though I have ollama installed

response = ollama.chat(model='mistral', messages=[
  {
    'role': 'user',
    'content': prompt,
  },
])
print(response['message']['content'])
