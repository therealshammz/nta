from scapy.layers.inet import IP, TCP, UDP

def parse_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        protocol = "TCP" if TCP in packet else "UDP" if UDP in packet else "Other"
        src_port = packet[TCP].sport if TCP in packet else packet[UDP].sport if UDP in packet else None
        dst_port = packet[TCP].dport if TCP in packet else packet[UDP].dport if UDP in packet else None
        return {
            "src_ip": ip_layer.src,
            "dst_ip": ip_layer.dst,
            "protocol": protocol,
            "src_port": src_port,
            "dst_port": dst_port,
            "length": len(packet)
        }
    return None
