def div_hash(string: str) -> int:
    key = 0
    for i in range(len(string)):
        key += ord(string[i]) * (2 ** i)
    return key % len(string)

def mul_hash(string: str) -> int:
    key = 0
    C = 0.1
    for i in range(len(string)):
        key += ord(string[i]) * (2 ** i)
    return len(string) * int((key * C))

def add_hash(string: str) -> int:
    sum = 0
    for i in range(len(string)):
        sum += ord(string[i]) * (2 ** i)
    return sum % 256

def crc32(data):
    crc = 0xffffffff
    for b in data:
        crc = crc ^ b
        for i in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xEDB88320
            else:
                crc = (crc >> 1)
    return crc ^ 0xffffffff

