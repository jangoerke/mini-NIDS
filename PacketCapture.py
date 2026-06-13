from scapy.all import sniff, IP, TCP
from collections import defaultdict
import threading
import queue

class PacketCapture:
    def __init__(self):
        self.packet_queue = queue.Queue()
        self.stop_capture = threading.Event()
    
    def packet_callback(self,pkt):
        if IP in pkt and TCP in pkt:
            self.packet_queue.put(pkt)
    
    def start_capture(self, interface='enp8s0'):
        def capture_thread():
            print("start sniffing")
            sniff(iface=interface,
                  prn=self.packet_callback,
                  store=0,
                  stop_filter=lambda _: self.stop_capture.is_set())
            
        self.capture_thread = threading.Thread(target=capture_thread)
        self.capture_thread.start()
            
    
    def end_capture(self):
        self.stop_capture.set()
        self.capture_thread.join()