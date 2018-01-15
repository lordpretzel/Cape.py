from six import string_types

CHAR_MASK = ((1 << 8) - 1)

# Compute a 1 byte version of the encryption key
def compute_reduced_key(key, length):
    reduced_key = 0
    # Reduced key computation
    for i in range(0, length):
        reduced_key = (reduced_key ^ (key[i] << (i % 8))) & CHAR_MASK
    return reduced_key

def normalize_bytes(key):
    if isinstance(key, string_types):
        return list(map(lambda c: ord(c), key))
    if isinstance(key, int):
        return [key]
    else:
        return key


class Cape:
    def __init__(self, key, salt=0):
        self.salt = normalize_bytes(salt)[0]
        self.key = normalize_bytes(key)
        self.length = len(key)
        self.reduced_key = compute_reduced_key(self.key, self.length)

    # Decrypt data (max 65535 characters)
    def decrypt(self, _source):
        source = normalize_bytes(_source)
        length = len(source) - 1
        saltKey = (self.salt ^ self.reduced_key) & CHAR_MASK
        iv = (source[-1] ^ length ^ self.key[(length ^ saltKey) % self.length]) & CHAR_MASK

        destination = [0] * length
        for i in range(0, length):
            destination[i] = (source[i] ^ iv ^ i ^ self.key[(saltKey ^ i) % self.length]) & CHAR_MASK
        return destination

    # Stream chipher, private key, initialization vector based encryption
    # algorithm (max 65535 characters)
    def encrypt(self, _source, iv):
        source = normalize_bytes(_source)
        length = len(source)
        saltKey = (self.salt ^ self.reduced_key) & CHAR_MASK
        destination = [0] * length
        destination.append((iv ^ length ^ self.key[(length ^ saltKey) % self.length]) & CHAR_MASK)
        for i in range(0, length):
            destination[i] = (source[i] ^ iv ^ i ^ self.key[(saltKey ^ i) % self.length]) & CHAR_MASK
        return destination

    # Symmetric chiper using private key, reduced key and optionally salt:
    def hash(self, _source):
        saltKey = (self.salt ^ self.reduced_key) & CHAR_MASK
        source = normalize_bytes(_source)
        destination = []
        for i in range(0, len(source)):
            iSaltKey = saltKey ^ i
            c = (source[i] ^ iSaltKey ^ self.key[iSaltKey % self.length]) & CHAR_MASK
            destination.append(c)
        return destination

def stringify(bytes):
    for c in bytes:
        if c < ord(' ') or c > ord('~'):
            return repr(bytes)
    return ''.join(map(lambda c: chr(c), bytes))
