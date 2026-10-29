from scapy.all import *

ps = rdpcap("./shark-on-wire-1-capture.pcap")



res = []
for pk in ps:
    if pk.haslayer("UDP") and pk.haslayer("IP") and pk['IP'].src == '10.0.0.2' and pk['IP'].dst == '10.0.0.12':
        res.append(pk['Raw'].load.decode())



for i in res:
    print(i, end= "")



