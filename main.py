from analyzer.sniffer import start_sniffing
import sys

if __name__ == '__main__':
    iface = sys.argv[1] if len(sys.argv) > 1 else 'wlo1'
    print(f"Starting packet capture on interface: {iface}")
    start_sniffing(interface=iface)
