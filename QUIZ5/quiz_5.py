
import time
import sys
from socket import *
from datetime import datetime

serverIP = sys.argv[1]
serverPort = int(sys.argv[2])

# UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
addr = (serverIP, serverPort)

list_rtts = []
packet_lost =0

for i in range(15):
    # current time
    time_stamp = datetime.now().isoformat(sep = ' ')[:-3]

    ping_message = f'{i+100} PING' + str(i) + ' ' + time_stamp + '\r\n'
    time_send = datetime.now()
    # send message
    clientSocket.sendto(ping_message.encode().addr)

    try:
        clientSocket.settimeout(0.4)
        response, serverAddress = clientSocket.revcfrom(1024)
        time_receive = datetime.now()

        rtt = round((time_receive - time_send).total_seconds() * 1000)
        list_rtts.append(rtt)

        print(f"{100+i} PING to {serverIP}, seq={i}, rtt={rtt} ms")
        clientSocket.settimeout(None)

    except timeout:
        packet_lost = packet_lost + 1
        print(f"{100+i} PING to {serverIP}, seq={i}, rtt= time out")

print("\n")
print(f'Minimum RTT = {min(list_rtts)} ms')
print(f'Maximum RTT = {max(list_rtts)} ms')
sum, len = sum(list_rtts), len(list_rtts)
print(f'Average RTT = {round(float(sum/len))} ms')
print(f'{float(packet_lost)/10 * 100}% of packets have been lost through the network')

