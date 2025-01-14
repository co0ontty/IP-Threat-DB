from ipdb import IPDB
import ipaddress
import readline
import time
import random

LIGHT_MALICIOUS    = 1
MEDIUM_MALICIOUS   = 2
CRITICAL_MALICIOUS = 3

level = [
    'UNKNOWN',
    'LIGHT_MALICIOUS',
    'MEDIUM_MALICIOUS',
    'CRITICAL_MALICIOUS'
]

def main():
    db = IPDB()
    black = 0
    for a in range(256):
        for b in range(256):
            db.set(b'0.0.%d.%d' % (a, b), 3)
            black += 1
    print('total %d black inserted' % black)
        
    cnt = 0
    fp = 0
    t = time.time_ns()
    for i in range(10000):
        v = db.get(b'0.0.%d.%d' % (
            random.randint(0, 255),
            random.randint(0, 255)
        ))
        cnt += 1
        if v != 3:
            fp += 1
    for i in range(10000):
        v = db.get(b'%d.%d.%d.%d' % (
            random.randint(1, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        ))
        cnt += 1
        if v != 0:
            fp += 1
    print('run %d times in %d ms, %d fp found, accuracy is %.2f%%' % (cnt, (time.time_ns() - t) // 10 ** 6, fp, (1 - fp / cnt) * 100))
        
if __name__ == '__main__':
    main()
