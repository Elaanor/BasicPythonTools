import scapy.all as scapy
import optparse

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ipaddress", dest="ip_address",help="Enter IP address")

    (user_input,arguments) = parse_object.parse_args()

    if not user_input.ip_address:
        print("Enter IP address")

    return user_input

def scan_my_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    combined_packet = broadcast_packet/arp_request_packet
    (answered_list,unanswered_list)=scapy.srp(combined_packet,timeout=1)
    #print(list(answered_list))
    answered_list.summary()

user_ip_address= get_user_input()
scan_my_network(user_ip_address.ip_address)