
import subprocess
import sys
import json
import numpy as np

import nvidiaLMPyTestGemma3Latest 
import nvidiaMLPyTest 
import nvidiaMLPyTestIpe

question = "Why is the sky blue?"
#question = input("Enter your question: ")
trialAnswer = input("How many trials do you want to run for each test?: ")
trialNum = int(trialAnswer)


#subprocess.run([sys.executable, "nvidiaMLPyTest.py"], input = question, text=True)
#subprocess.run([sys.executable, "nvidiaMLPyTestIpe.py"], input = question, text=True)


## putting everything for gemma3:latest test below
def gemma3_test():
    gemma3_list_gpu_util = []
    for i in range(trialNum):
        result = subprocess.run([sys.executable, "nvidiaLMPyTestGemma3Latest.py"], input = question, text=True, capture_output=True)

        ## Reading the JSON files to get GPU stats
        with open("gpu_stats.json") as f:
            stats = json.load(f)


        print("This is gpu_util:", stats["gpu_util"], "This is vram_util:", stats["vram_used"])
    
        gemma3_list_gpu_util.append(stats["gpu_util"])


    print(gemma3_list_gpu_util)
    gemma3_arr = np.array(gemma3_list_gpu_util, dtype=float)
    gemma3_list_gpu_util_avg = np.mean(gemma3_arr)
    print(f"Average GPU Utilization for gemma3:latest over {trialNum} trials: {gemma3_list_gpu_util_avg:.2f}%")

def ollama_model_test(model_name):
    gpu_util_list = []
    for i in range(trialNum):
        result = subprocess.run([sys.executable, model_name + ".py"], input = question, text=True, capture_output=True)

        ## Reading the JSON files to get GPU stats
        with open(model_name + "_gpu_stats.json") as f:
            stats = json.load(f)


        print("This is gpu_util:", stats["gpu_util"], "This is vram_util:", stats["vram_used"])
    
        gpu_util_list.append(stats["gpu_util"])


    print(gpu_util_list)
    gemma3_arr = np.array(gpu_util_list, dtype=float)
    gpu_util_avg = np.mean(gemma3_arr)
    print(f"Average GPU Utilization for {model_name} over {trialNum} trials: {gpu_util_avg:.2f}%")


#gemma3_test()

ollama_model_test("nvidiaLMPyTestGemma3Latest")
print("All tests completed successfully.")
