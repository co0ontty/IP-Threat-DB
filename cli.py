from ipdb import IPDB
import ipaddress
import readline



level = [
    'UNKNOWN',
    'LIGHT_MALICIOUS',
    'MEDIUM_MALICIOUS',
    'CRITICAL_MALICIOUS'
]

def main():
    db = IPDB()
    db.load('./ip-threat.db')

    while True:
        ip = input('(IPDB) > ')
        print('%s => %s' % (ip, level[db.get(ip.encode())]))


if __name__ == '__main__':
    main()
