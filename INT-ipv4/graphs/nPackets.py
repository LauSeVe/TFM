from scapy.all import *
import pandas as pd
import numpy as np
import sys


def analyze_pcap(file_path):
    packets = rdpcap(file_path)
    times = []
    #ping_packets = [pkt for pkt in packets if ICMP in pkt if pkt.haslayer(ICMP) and len(pkt[ICMP].payload) == 56]
    #num_ping_packets = len(ping_packets)    
    #ping_packets_sizes = [len(pkt) for pkt in ping_packets] if ping_packets else [0]
    #ping_values = [num_ping_packets, np.min(ping_packets_sizes), np.mean(ping_packets_sizes), np.max(ping_packets_sizes)]

    iperf_packets = [pkt for pkt in packets if UDP in pkt if pkt.haslayer(UDP)]
    num_iperf_packets = len(iperf_packets)    
    iperf_packet_sizes = [len(pkt) for pkt in iperf_packets] if iperf_packets else [0]
    iperf_values = [num_iperf_packets, np.min(iperf_packet_sizes), np.mean(iperf_packet_sizes), np.max(iperf_packet_sizes)]
    
    TYPE_EPHeader = 0x93
    ep_packets = [pkt for pkt in packets if IP in pkt and pkt[IP].proto == TYPE_EPHeader]
    num_ep_packets = len(ep_packets)    
    ep_packet_sizes = [len(pkt) for pkt in ep_packets] if ep_packets else [0]
    ep_values = [num_ep_packets, np.min(ep_packet_sizes), np.mean(ep_packet_sizes), np.max(ep_packet_sizes)]
    
    #data = {
    #'Metric': ['Number of Packets', 'Min Size', 'Mean Size', 'Max Size'],
    #'Ping': ping_values,
    #'BgT': iperf_values,
    #'TCP': tcp_values,
    #'UDP': udp_values,
    #'EP': ep_values
    #}

    times = [ep_values,iperf_values]

    print(times)
    return times

def main():
    if len(sys.argv) != 2:
        print("python3 nPackets.py <pcap>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    output = analyze_pcap(file_path)


if __name__ == "__main__":
    main()
