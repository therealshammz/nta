from scapy.all import sniff
from analyzer.parser import parse_packet
from analyzer.logger import log_packet

def start_sniffing(interface='wlo1'):  # update default to your actual interface
    sniff(iface=interface, prn=process_packet, store=False)

def process_packet(packet):
    parsed = parse_packet(packet)
    if parsed:
        log_packet(parsed)
        print(parsed)  # 👈 this line shows output in terminal
