#!/usr/bin/env python3
import sys

from scapy.all import *
from scapy.layers.inet import _IPOption_HDR


def get_if():
    ifs = get_if_list()
    iface = None
    for i in get_if_list():
        if "enp7s0" in i:
            iface = i
            break
    if not iface:
        print("Cannot find enp7s0 interface")
        exit(1)
    return iface

TYPE_EPHeader = 0x93

class EPHeader(Packet):
    name = "EPHeader"
    fields_desc = [
        BitField("hawkID", 0, 16),
        BitField("exercise", 0, 4),
        BitField("ethernet", 0, 1),
        BitField("ipv4", 0, 1),
        BitField("ipv6", 0, 1),
        BitField("correct", 0, 1),
        StrFixedLenField("info", b"\x00" * 20, length=20),
    ]

class SwitchTrace(Packet):
    fields_desc = [
        IntField("swid", 0),
        IntField("qdepth", 0)
    ]
    def extract_padding(self, p):
        return "", p

class IPOption_MRI(IPOption):
    name = "MRI"
    option = 31
    fields_desc = [
        _IPOption_HDR,
        FieldLenField("length", None, fmt="B", length_of="swtraces", adjust=lambda pkt, l: l * 2 + 4),
        ShortField("count", 0),
        PacketListField("swtraces", [], SwitchTrace, count_from=lambda pkt: (pkt.count * 1))
    ]

def handle_pkt(pkt):
    if IP in pkt and pkt[IP].proto == TYPE_EPHeader:
        packet_bytes = raw(pkt)
        packet_hex = packet_bytes.hex()
        print(packet_hex)
        wrpcap("./output.pcap", pkt, append=True)
        sys.stdout.flush()

def main():
    iface = get_if()  # Use the returned interface from get_if()
    print("sniffing on %s" % iface)
    sys.stdout.flush()
    sniff(iface=iface, prn=lambda x: handle_pkt(x))

if __name__ == '__main__':
    bind_layers(IP, EPHeader, proto=TYPE_EPHeader)
    main()
