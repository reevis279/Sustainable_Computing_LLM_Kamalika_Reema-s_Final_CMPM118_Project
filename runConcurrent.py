
import subprocess
import sys
import json
import numpy as np

import nvidiaLMPyTestGemma3Latest 
import nvidiaMLPyTestGemma2b 
import nvidiaMLPyTestIpe

#question = "Why is the sky blue?"
question = input("Enter your question: ")
trialAnswer = input("How many trials do you want to run for each test?: ")
trialNum = int(trialAnswer)


#subprocess.run([sys.executable, "nvidiaMLPyTest.py"], input = question, text=True)
#subprocess.run([sys.executable, "nvidiaMLPyTestIpe.py"], input = question, text=True)


## putting main function below 

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


print("Starting tests for gemma3:Latest model...")
ollama_model_test("nvidiaLMPyTestGemma3Latest")

print("Starting tests for gemma:2b model...")
ollama_model_test("nvidiaMLPyTestGemma2b")

print("Starting tests for ipe:latest model...")
ollama_model_test("nvidiaMLPyTestIpe")

print("Starting tests for gemma2:Latest model...")
ollama_model_test("nvidiaMLPyTestGemma2Latest")

print("All tests completed successfully.")
