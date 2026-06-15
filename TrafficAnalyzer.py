from collections import defaultdict

class TrafficAnalyzer:
    def __init__(self):
        self.flow_stats = defaultdict(lambda:{
            'packet_count': 0,
            'bin_length': 0,
            'start_time': None,
            'end_time': None
        })