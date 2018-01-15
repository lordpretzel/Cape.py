from cape import Cape, stringify


cape = Cape('ANY ENCRYPTION KEY', 'S')


def test_hashing_string():
    input = 'CRYPTMEPLEASE'
    expected = [11, 6, 8, 1, 15, 6, 6, 27, 1, 112, 18, 10, 16]
    assert cape.hash(input) == expected

def test_hashing_string():
    input = 'CRYPTMEPLEASE'
    expected = [11, 6, 8, 1, 15, 6, 6, 27, 1, 112, 18, 10, 16]
    assert cape.hash(input) == expected

def test_hashing_bytes():
    input = [67, 82, 89, 80, 84, 77, 69, 80, 76, 69, 65, 83, 69]
    expected = [11, 6, 8, 1, 15, 6, 6, 27, 1, 112, 18, 10, 16]
    assert cape.hash(input) == expected

def test_hashing_symmetry_stringify():
    input = 'CRYPTMEPLEASE'
    assert stringify(cape.hash(cape.hash(input))) == input

def test_hashing_symmetry_bytes():
    input = [67, 82, 89, 80, 84, 77, 69, 80, 76, 69, 65, 83, 69]
    assert cape.hash(cape.hash(input)) == input


def test_encrypt_string():
    input = 'CRYPTMEPLEASE'
    iv = 381
    expected = [106, 103, 105, 96, 110, 103, 103, 122, 96, 17, 115, 107, 113, 41]
    assert cape.encrypt(input, iv) == expected

def test_encrypt_bytes():
    input = [67, 82, 89, 80, 84, 77, 69, 80, 76, 69, 65, 83, 69]
    iv = 381
    expected = [106, 103, 105, 96, 110, 103, 103, 122, 96, 17, 115, 107, 113, 41]
    assert cape.encrypt(input, iv) == expected


def test_decrypt():
    input = [106, 103, 105, 96, 110, 103, 103, 122, 96, 17, 115, 107, 113, 41]
    expected = [67, 82, 89, 80, 84, 77, 69, 80, 76, 69, 65, 83, 69]
    assert cape.decrypt(input) == expected

def test_decrypt_stringify():
    input = [106, 103, 105, 96, 110, 103, 103, 122, 96, 17, 115, 107, 113, 41]
    expected = 'CRYPTMEPLEASE'
    assert stringify(cape.decrypt(input)) == expected


def test_encrypt_decrypt():
    input = 'CRYPTMEPLEASE'
    expected = [67, 82, 89, 80, 84, 77, 69, 80, 76, 69, 65, 83, 69]
    iv = 26611
    assert cape.decrypt(cape.encrypt(input, iv)) == expected

def test_encrypt_decrypt_stringify():
    input = 'CRYPTMEPLEASE'
    iv = 26611
    assert stringify(cape.decrypt(cape.encrypt(input, iv))) == input
