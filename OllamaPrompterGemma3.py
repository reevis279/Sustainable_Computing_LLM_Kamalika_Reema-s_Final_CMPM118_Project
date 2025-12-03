##Make sure to run this code within a virtual environment in WSL because that's where ollama is installed.

from ollama import chat
from ollama import ChatResponse
#First make sure to run this code within a virtual environment
#Ask user to input promt for ollama model
prompt = "Why is the sky blue?"
print(f"The prompt is: {prompt}")

#
#If ollama is installed, ask it the prompt.
import ollama #error here, even though I have ollama installed
#Figure out how to run inside virtual environment later to fix

#Work on the below later
#import subprocess.run(["python",tutorialForSubprocesses.py])

response = ollama.chat(model='gemma3:latest', messages=[  
  {
    'role': 'user',
    'content': prompt,
  },
])
print("\nModel is gemma3:latest\n")
print(response['message']['content'])