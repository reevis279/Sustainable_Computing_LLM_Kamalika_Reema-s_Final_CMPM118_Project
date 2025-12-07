
import subprocess
import sys
import json

import nvidiaLMPyTestGemma3Latest 
import nvidiaMLPyTest 
import nvidiaMLPyTestIpe

question = "Why is the sky blue?"
#question = input("Enter your question: ")
#number = input("How many trials do you want to run for each test?: ")

result = subprocess.run([sys.executable, "nvidiaLMPyTestGemma3Latest.py"], input = question, text=True, capture_output=True)

#subprocess.run([sys.executable, "nvidiaMLPyTest.py"], input = question, text=True)
#subprocess.run([sys.executable, "nvidiaMLPyTestIpe.py"], input = question, text=True)

## Reading the JSON files to get GPU stats
with open("gpu_stats.json") as f:
    stats = json.load(f)


print("This is gpu_util:", stats["gpu_util"], "This is vram_util:", stats["vram_used"])
gemma3_dict = []
 
print("All tests completed successfully.")
