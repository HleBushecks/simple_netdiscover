import os
import time
from threading import Thread

pattern = input("write ip pattern(192.168.1): ")
count = 0
ip = []
th = None


def ping(comm):
    global count, ip
    result = os.popen(f"ping -b -c 1 -w 1 {comm}").read()
    if "64 bytes" in result:
        print(f"{comm}:true")
        count += 1
        ip.append(f"{comm}")
    # else:
    #     print(f"{command}:false")


for i in range(0, 256):
    command = f"{pattern}.{i}"
    th = Thread(target=ping, args=(command,))
    th.start()
    time.sleep(0.01)

while th.is_alive():
    time.sleep(2)

print(count)

with open(f"ip_{pattern}.txt", "w") as file:
    for i in ip:
        file.write(i + "\n")
