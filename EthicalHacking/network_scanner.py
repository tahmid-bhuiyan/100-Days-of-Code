# #!/isr/bin/env python
# NETWORK SCANNER PROGRAM
#-- PERSONAL NOTES --
# TO USE ON REAL DEVICES, PLUG IN A WIRELESS ADAPTER
# ARP REQUESTS GET MAC ADDRESSES OF DEVICES ON A NETWORK BY ASKING "WHO HAS THIS IP ADDRESS?"
# '10.0.2.1/24' scans for ip addresses from 10.0.2.1-254
#-- END OF NOTES --

import scapy.all as scapy
import argparse

def get_arguments():
    # argparse asks for arguments after giving filename
    # dest value stores user input value
    parser = argparse.ArgumentParser()
    # when in cmd, python network_scanner.py -t __
    parser.add_argument('-t', '--target', dest='network', help='Get MAC Addresses of this network')
    # stores user input values (options), '-i, --mac etc. into (arguments)
    (options, arguments) = parser.parse_args()
    # if interface or new_mac values are not inputted, raise an error
    if not options.network:
        parser.error('[-] Please specify an network, use --help for more info')
    return options.network
def scan(ip):
# CREATES A BROADCAST WITH DESTINATION MAC ADDRESS (SEND TO ALL DEVICES IN NETWORK)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
# CREATES AN ARP REQUEST PACKET, pdst IS IP FIELD
    arp_request = scapy.ARP(pdst=ip)
# USE (variable name).summary() TO SEE WHAT INFO THE VARIABLE HOLDS
# USE scapy.ls(__) TO VIEW ALL ARGUMENT OPTIONS FOR INPUTTED CLASS
# USE (variable name).show() TO VIEW SPECIFIC DETAILS
# COMBINES ARP REQUEST PACKET AND DESTINATION (BROADCAST)
    arp_request_broadcast = broadcast/arp_request
# SENDS AND RECEIVES PACKETS, RETURNS ANSWERED/UNANSWERED LISTS, USE TIMEOUT TO WAIT FOR RESPONSES FOR 1 SEC (OTHERWISE INFINITE LOOP)
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)
# PRINTS IP (psrc) AND MAC(hwsrc) of each answered
    print('IP\t\t\tMAC\n--------------------------------------------------')
# CREATES A LIST TO HOLD IP/MAC ADDRESS DICTIONARIES OF EACH CLIENT
    client_lst = []
    for element in answered:
        dict = {'ip':element[1].psrc, 'mac':element[1].hwsrc}
        client_lst.append(dict)
        print(element[1].psrc + '\t\t\t' + element[1].hwsrc)
arg = get_arguments()
scan(arg)
