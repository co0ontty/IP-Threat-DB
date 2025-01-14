from ipdb import IPDB
import ipaddress

LIGHT_MALICIOUS    = 1
MEDIUM_MALICIOUS   = 2
CRITICAL_MALICIOUS = 3

def build():
    db = IPDB()

    with open('./50k.txt') as f:
        for line in f:
            network = ipaddress.ip_network(line.strip())
            for ip in network:
                db.set((str(ip).encode()), LIGHT_MALICIOUS)

    with open('./20k.txt') as f:
        for line in f:
            network = ipaddress.ip_network(line.strip())
            for ip in network:
                db.set((str(ip).encode()), MEDIUM_MALICIOUS)

    with open('./5k.txt') as f:
        for line in f:
            network = ipaddress.ip_network(line.strip())
            for ip in network:
                db.set((str(ip).encode()), CRITICAL_MALICIOUS)


    db.dump('ip-threat.db')


if __name__ == '__main__':
    build()
