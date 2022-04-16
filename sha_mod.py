def sha1(data):
    bytes = ""

    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    for n in range(len(data)):
        bytes += '{0:08b}'.format(ord(data[n]))
    bits = bytes + "1"
    pBits = bits
    while len(pBits) % 512 != 448:
        pBits += "0"
    pBits += '{0:064b}'.format(len(bits)-1)

    def chunks(l, n):
        return [l[i:i+n] for i in range(0, len(l), n)]

    def leftrotate(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xffffffff

    for c in chunks(pBits, 512): 
        words = chunks(c, 32)
        w = [0] *   80
        for n in range(0, 16):
            w[n] = int(words[n], 2)
        for i in range(16, 80):
            w[i] = leftrotate((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1)  

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        for i in range(0, 80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d) 
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = leftrotate(a, 5) + f + e + k + w[i] & 0xffffffff
            e = d
            d = c
            c = leftrotate(b, 30)
            b = a
            a = temp

        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff

    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

def hex_to_bin(data):
    b = "{0:08b}".format(int(data, 16))
    return b.zfill(160)

def shift(hash, n):
    x = hash[:n]
    y = hash[n+1:]
    return x + y

def hash_shift(split_hash, n):
    x = sha1(sha1(split_hash))
    x1 = shift(x, n)
    return hex_to_bin(x1)

def split(data):
    data = hex_to_bin(sha1(data)) #sha1 returns hex, convert to binary, this yields 160bits length data
    l= data[:80]
    r = data[80:]
    l1 = hash_shift(l, 5)
    r1 = hash_shift(r, 10)
    l11 = l1[80:]
    l12 = l1[:80]
    r11 = r1[80:]
    r12 = r1[:80]
    x1 = int(l11, 16) ^ int(l12, 16)
    x1 = '{:x}'.format(x1)
    x2 = int(r11, 16) & int(r12, 16)
    x2 = '{:x}'.format(x2)
    # print(x1 + x2)
    return x1 + x2

def result(text):
    return sha1(split(text))


# print(result('hello'))


