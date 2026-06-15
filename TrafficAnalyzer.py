from collections import defaultdict
from scapy.all import IP, TCP

class TrafficAnalyzer:
    def __init__(self):
        self.flow_stats = defaultdict(lambda:{
            'packet_count': 0,
            'bin_length': 0,
            'start_time': None,
            'end_time': None
        })
    
    def analyze_pkt(self, pkt):
        if IP in pkt and TCP in pkt:
            source_ip = pkt[IP].src
            dest_ip = pkt[IP].dst
            source_port = pkt[TCP].sport
            dest_port = pkt[TCP].dport

            flow_key = (source_ip,source_port,dest_ip,dest_port)

            stats = self.flow_stats[flow_key]
            stats['packer_count'] += 1
            stats['bin_length'] += len(pkt)

            current_time = pkt.time

            if stats['start_time'] is None:
                stats['start_time'] = current_time
            stats['end_time'] = current_time
