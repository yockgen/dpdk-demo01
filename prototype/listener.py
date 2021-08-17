import scapy.all as scapy
import time

def show_payload(pkt):
	print (str(pkt.payload))

for x in range (0,1000):
	capture = scapy.sniff (count=5, prn=show_payload, filter="ether dst 08:00:27:ac:9a:90") #change mac to your dst mac!!!
	capture.summary()
	time.sleep(0.5)
        
