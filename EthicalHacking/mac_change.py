# #!/isr/bin/env python
# MAC CHANGER PROGRAM
#-- PERSONAL NOTES --
#MAC address is physical, hard address for a device
#Packets sent through a network have a source/destination mac, which is on the ethernet layer
#Changing mac address makes you more anonymous,impersonate other devices
#eth0 is an interface & means device is connected to NAT network
#change mac address by disabling the interface, change it, then turn on
#-- END OF NOTES --
import subprocess
import optparse
import re

#ifconfig __ in terminal to check interfaces
#unsecure version, person can run their own commands using semicolon
# subprocess.call('ifconfig ' + interface + ' down', shell=True)
# subprocess.call('ifconfig ' + interface + ' hw ether ' + new_mac, shell=True)
# subprocess.call('ifconfig ' + interface + ' up', shell=True)

def get_arguments():
    # optparse asks for arguments after giving filename
    # dest value stores user input value
    parser = optparse.OptionParser()
    # when in cmd, python mac_change.py interface __ new_mac __
    parser.add_option('-i', '--interface', dest='interface', help='Interface to change its MAC address')
    parser.add_option('-m', '--mac', dest='new_mac', help='New MAC address')
    # stores user input values (options), '-i, --mac etc. into (arguments)
    (options, arguments) = parser.parse_args()
    #if interface or new_mac values are not inputted, raise an error
    if not options.interface:
        parser.error('[-] Please specify an interface, use --help for more info')
    elif not options.new_mac:
        parser.error('[-] Please specify a new_mac, use --help for more info')
    return options
def change_mac(interface, new_mac):
    print('Changing MAC address for ' + interface + ' to ' + new_mac)
    #secure version, every word is part of the same command, can't use ls
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])
def current_mac():
    # returns string value of everything outputted by ifconfig and stores it in a variable, executes 'ifconfig ___'
    ifconfig_result = subprocess.check_output(['ifconfig', options.interface])
    mac_address_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(ifconfig_result))
    # checks to see if mac address was found, then print
    if mac_address_search_result:
        # re.search can return multiple searches, so .group is used to get the first(and only) one
        return mac_address_search_result.group(0)
    else:
        print('[-] Could not read MAC address.')
options = get_arguments()
print('Your current MAC address is: {}'.format(str(current_mac())))
#options.__ gets user input values from get_arguments
change_mac(options.interface, options.new_mac)
print('Your current MAC address is: {}'.format(current_mac()))
