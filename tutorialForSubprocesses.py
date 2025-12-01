from time import sleep

print("Starting timer of 5 seconds")
for _ in range(5, 0, -1):
    print(".", end="", flush=True)
    sleep(1)

print("Done!")