import os
import time
from threading import Thread

pattern = input("write ip pattern(192.168): ")
count = 0
ip_array = []
th = None


def ping(ip_addres):
    global count, ip_array
    result = os.popen(f"ping -b -c 1 -w 1 {ip_addres}").read()
    if "64 bytes" in result:
        print(f"{ip_addres}:true")
        count += 1
        ip_array.append(f"{ip_addres}")
    # else:
    #     print(f"{ip_addres}:false")


for ii in range(0, 256):
    for i in range(0, 256):
        command = f"{pattern}.{ii}.{i}"
        th = Thread(target=ping, args=(command,))
        th.start()
        time.sleep(0.01)

while th.is_alive():
    time.sleep(2)

print(count)

with open(f"ip_{pattern}.txt", "w") as file:
    for i in ip_array:
        file.write(i + "\n")
