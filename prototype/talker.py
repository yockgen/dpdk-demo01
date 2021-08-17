import scapy.all as scapy
import time


for x in range (0,1000):
	srcMc = '08:00:27:73:58:26'
	dstMc = '08:00:27:ac:9a:90' 
	packet = scapy.Ether(src=srcMc,dst=dstMc,type=0x0842)/"yockgen yockgen"
	packet.show()
	scapy.sendp(packet, iface="enp0s8")
	#time.sleep(1)
