import hashlib

SIZE = 256 * 256 * 256

class IPDB:
    def __init__(self):
        self.data = bytearray(SIZE // 4 * 5)

    def ipToKey(self, ip):
        md5 = hashlib.md5(ip).digest()
        for i in range(1000):
            md5 = hashlib.md5(md5).digest()
        keys = []
        for i in range(5):
            key = 0
            key += md5[i * 3 + 0] * 256 ** 0
            key += md5[i * 3 + 1] * 256 ** 1
            key += md5[i * 3 + 2] * 256 ** 2
            keys.append(key)
        return keys

    def setMap(self, table, key, flag):
        offset = table * SIZE // 4 + key // 4
        v = self.data[offset]
        v &= [0b11111100, 0b11110011, 0b11001111, 0b00111111][key % 4]
        v |= flag << (key % 4) * 2
        self.data[offset] = v

    def set(self, ip, flag):
        keys = self.ipToKey(ip)
        for i in range(len(keys)):
            self.setMap(i, keys[i], flag)

    def dump(self, path):
        with open(path, 'wb') as f:
            f.write(self.data)

    def getMap(self, table, key):
        offset = table * SIZE // 4 + key // 4
        v = self.data[offset]
        v &= [0b00000011, 0b00001100, 0b00110000, 0b11000000][key % 4]
        v >>= key % 4 * 2
        return v

    def get(self, ip):
        keys = self.ipToKey(ip)
        value = -1
        for i in range(len(keys)):
            v = self.getMap(i, keys[i])
            if value == -1:
                value = v
            elif value != v:
                return 0
        return value

    def load(self, path):
        with open(path, 'rb') as f:
            self.data = bytearray(f.read())

