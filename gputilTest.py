import time
import threading
import GPUtil as GPU
import ollama 

monitoring_active = True
max_gpu_usage_percent = 0.0
max_vram_usage_mb = 0.0
gpu_index = 0

def monitor_ollama_resources():
    global monitoring_active
    global max_gpu_usage_percent
    global max_vram_usage_mb
    
    try:
        gpus = GPU.getGPUs()
    except Exception:
        print("\nCannot find or access NVIDIA GPUs (nvidia-smi error). Monitoring terminated.")
        monitoring_active = False
        return

    if not gpus:
        print("\nNo NVIDIA GPUs detected. Cannot perform GPU monitoring.")
        monitoring_active = False
        return

    if gpu_index >= len(gpus):
        print(f"\nGPU index {gpu_index} not found. Only {len(gpus)} GPUs detected.")
        monitoring_active = False
        return
        
    print("\n--- Background GPU Monitoring Started (Sampling every 0.1s) ---")
    print(f"--- Monitoring GPU {gpu_index}: {gpus[gpu_index].name} ---")

    while monitoring_active:
        try:
            gpus = GPU.getGPUs()
            gpu_data = gpus[gpu_index]

            gpu_load = gpu_data.load * 100 
            vram_used = gpu_data.memoryUsed

            if gpu_load > max_gpu_usage_percent:
                max_gpu_usage_percent = gpu_load
            if vram_used > max_vram_usage_mb:
                max_vram_usage_mb = vram_used

            time.sleep(0.1)

        except Exception as e:
            print(f"\nMonitoring error: {e}. Stopping thread.")
            monitoring_active = False
            break
        
    print("--- Background GPU Monitoring Finished ---\n")


prompt = "Why is the sky blue?"
print(f"The prompt is: {prompt}")

monitor_thread = threading.Thread(target=monitor_ollama_resources)
monitor_thread.start()

time.sleep(1)

response = ollama.chat(model='gemma:2b', messages=[  
  {
    'role': 'user',
    'content': prompt,
  },
])

monitoring_active = False
monitor_thread.join()

print("\nModel is gemma:2b\n")
print(response['message']['content'])

print("\n\n#####################################################")
print("## OLLAMA CHAT GPU RESOURCE USAGE (MAX) ##")
print(f"## Max GPU Utilization: {max_gpu_usage_percent:.2f}%")
print(f"## Max VRAM Used: {max_vram_usage_mb:.2f} MB")
print("#####################################################\n")
