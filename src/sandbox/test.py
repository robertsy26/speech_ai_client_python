import subprocess
import time

process = subprocess.Popen(['python', 'test2.py'], stdin=subprocess.PIPE, text=True)

while True:
    time.sleep(2)
    process.stdin.write("enter\n")
    process.stdin.flush()
    print("enter ran")
