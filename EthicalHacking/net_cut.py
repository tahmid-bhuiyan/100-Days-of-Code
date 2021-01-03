#!usr/bin/env python
# NETWORK CUT PROGRAM
#-- PERSONAL NOTES --
# THIS PROGRAM RECIEVES REQUEST/RESPONSE PACKETS WHICH CAN BE MODIFIED IN A QUEUE BEFORE -
# - FORWARDING TO NEXT DEVICE
#-- END OF NOTES --

# FIRST ENTER THESE COMMANDS IN THE TERMINAL:
# 1. iptables -I FORWARD -j NFQUEUE --queue-num 0
#   - CREATES A QUEUE ON YOUR DEVICE, CAN USE ANY NUMBER (IN THIS CASE 0)
# 2. pip install netfilterqueue
#   - INSTALLS THE QUEUE MODULE

#USED TO CREATE A QUEUE
import netfilterqueue

# prints the packet that flows into the queue
def process_packet(packet):
    print(packet)

# creates an instance of a queue
queue = netfilterqueue.NetfilterQueue()
# binds the queue created in this program with the queue on actual --
# -- kali machine (created with the above terminal command)
# calls the process_packet function everytime a packet enters the queue
queue.bind(0, process_packet)
# runs the queue
queue.run()