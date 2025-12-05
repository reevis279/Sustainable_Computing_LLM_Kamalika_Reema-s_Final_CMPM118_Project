import ollama
from ollama import chat
from ollama import ChatResponse
import psutil
import os
import time

def log_ollama_server_usage(stage):
    ollama_process = None
    # Look for the Ollama process by name
    for p in psutil.process_iter(['name', 'cpu_percent', 'memory_info']):
        # Ollama's process name is usually 'ollama' or is a ollama.exe
        if 'ollama' in p.info['name'].lower():
            ollama_process = p
            break

    if not ollama_process:
        print(f"\n--- Resource Log: {stage} ---")
        print("Ollama server process not found. Cannot log its resources.")
        print("----------------------------\n")
        return

    try:
        ollama_process.cpu_percent()
        time.sleep(0.01) 
        cpu_usage = ollama_process.cpu_percent()
        
        memory_info = ollama_process.memory_info()
        memory_usage_mb = memory_info.rss / (1024 * 1024) 

        print(f"\n--- Resource Log: {stage} (Ollama Server) ---")
        print(f"PID: {ollama_process.pid}")
        print(f"CPU Usage: {cpu_usage:.2f}%")
        print(f"Memory Usage (RSS): {memory_usage_mb:.2f} MB")
        print("----------------------------\n")
        
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        print("\nCould not get resource details for the Ollama process.")


prompt = "Why is the sky blue?"
print(f"The prompt is: {prompt}")
import ollama
log_ollama_server_usage("BEFORE OLLAMA CHAT (Idle)")
response = ollama.chat(model='gemma:2b', messages=[  
  {
    'role': 'user',
    'content': prompt,
  },
])

log_ollama_server_usage("AFTER OLLAMA CHAT (Work Complete)")
print("\nModel is gemma:2b\n")
print(response['message']['content'])
