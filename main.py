import PacketCapture
import queue

def main():
    pkt_capture = PacketCapture.PacketCapture()
    pkt_capture.start_capture()
    while True:
        try:
            pkt = pkt_capture.packet_queue.get(timeout=1)
            print(pkt.summary())
        except queue.Empty:
            continue
        except KeyboardInterrupt:
            pkt_capture.stop_capture()
            break


if __name__ == "__main__":
    main()
