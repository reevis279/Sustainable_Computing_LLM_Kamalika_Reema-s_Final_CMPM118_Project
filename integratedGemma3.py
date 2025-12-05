from ollama import chat
from ollama import ChatResponse
import psutil
import os
import time

def log_resource_usage(stage):
    pid = os.getpid()
    p = psutil.Process(pid)
    p.cpu_percent()
    time.sleep(5)
    cpu_usage = p.cpu_percent()
    memory_info = p.memory_info()
    memory_usage_mb = memory_info.rss / (1024 * 1024) 

    print(f"\n--- Resource Log: {stage} ---")
    print(f"PID: {pid}")
    print(f"CPU Usage: {cpu_usage:.2f}%")
    print(f"Memory Usage (RSS): {memory_usage_mb:.2f} MB")
    print("----------------------------\n")

prompt = "Why is the sky blue?"
print(f"The prompt is: {prompt}")

import ollama

log_resource_usage("BEFORE OLLAMA CHAT")

response = ollama.chat(model='gemma:2b', messages=[  
  {
    'role': 'user',
    'content': prompt,
  },
])

log_resource_usage("AFTER OLLAMA CHAT")

print("\nModel is gemma:2b\n")
print(response['message']['content'])