
#asking prompt from gemma:2b and monitoring GPU usage with pynvml

import time
import threading
import ollama 
import pynvml

# Global variables to track state and maximum usage
monitoring_active = True    
max_gpu_usage_percent = 0.0
max_vram_usage_mb = 0.0
gpu_index = 0

def monitor_ollama_resources_nvml():
    global monitoring_active
    global max_gpu_usage_percent
    global max_vram_usage_mb

    try:
        # Initialize NVML and get handle for the target GPU
        pynvml.nvmlInit()
        handle = pynvml.nvmlDeviceGetHandleByIndex(gpu_index)
        gpu_name = pynvml.nvmlDeviceGetName(handle)
        
    except pynvml.NVMLError as e:
        print(f"\nCannot initialize NVML or access GPU {gpu_index}: {e}")
        monitoring_active = False
        return
        
    print("\n--- Background GPU Monitoring Started (NVML) ---")
    print(f"--- Monitoring GPU {gpu_index}: {gpu_name} ---")

    while monitoring_active:
        try:
            # Get Utilization Rates (GPU load)
            utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
            gpu_load = utilization.gpu 
            
            # Get Memory Info (VRAM used)
            memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
            # Memory is reported in bytes, convert to MB
            vram_used = memory_info.used / (1024 * 1024) 

            # Update maximums
            if gpu_load > max_gpu_usage_percent:
                max_gpu_usage_percent = gpu_load
            if vram_used > max_vram_usage_mb:
                max_vram_usage_mb = vram_used

            time.sleep(0.1)

        except pynvml.NVMLError as e:
            print(f"\nMonitoring error: {e}. Stopping thread.")
            monitoring_active = False
            break
        
    pynvml.nvmlShutdown() # Shut down NVML when finished
    print("--- Background GPU Monitoring Finished ---\n")

def GPU_info_before():
    print("\n\n#####################################################")
    print("## GPU RESOURCE USAGE (MAX) before Ollama chat##")
    print(f"## Max GPU Utilization: {max_gpu_usage_percent:.2f}%")
    print(f"## Max VRAM Used: {max_vram_usage_mb:.2f} MB")
    print("#####################################################\n")    

if __name__ == "__main__":
    GPU_info_before()
    
    prompt = "Why is the sky blue?"
    print(f"The prompt is: {prompt}")

    monitor_thread = threading.Thread(target=monitor_ollama_resources_nvml)
    monitor_thread.start()

    # Give the thread a moment to find the process and set the baseline
    time.sleep(1)

    # Execute the resource-intensive chat call in the main thread
    response = ollama.chat(model='ipe:latest', messages=[  
    {
        'role': 'user',
        'content': prompt,
    },
    ])

    # Stop the monitoring thread
    monitoring_active = False
    monitor_thread.join()
    def print_info():
        print("\nModel is ipe:latest\n")
        print(response['message']['content'])

        print("\n\n#####################################################")
        print("## OLLAMA CHAT GPU RESOURCE USAGE (MAX) ##")
        print(f"## Max GPU Utilization: {max_gpu_usage_percent:.2f}%")
        print(f"## Max VRAM Used: {max_vram_usage_mb:.2f} MB")
        print("#####################################################\n")

    #print_info()# Call the function to print info