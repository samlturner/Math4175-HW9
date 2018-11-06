s_box = [0xE, 0x4, 0xD, 0x1, 0x2, 0xF, 0xB, 0x8, 0x3, 0xA, 0x6, 0x6, 0xC, 0x5, 0x9, 0x0, 0x7]
pi_p = [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]
Nr = 4

def key_gen(b_key, key_num):
    index = (4 * key_num) - 3
    # return ((b_key >> index)|(b_key << (32 - index)) & 0xFFFFFFFF) >> 16
    return ((b_key << index) | (b_key >> (32 - index))) >> 16


# Encrypts the plaintext using the provided key
def encrypt_SPN(p, key):
    w = p
    for r in range(1, Nr):
        u = w ^ key_gen(b_key, r)
        v = e_sbox(u)
        w = e_permutation(v)
    u = w ^ key_gen(b_key, Nr)
    v = e_sbox(u)
    c = v ^ key_gen(b_key, Nr + 1)
    return c


def e_sbox(u):
    mask = 15
    v = 0
    for i in range(0, 4):
        temp = s_box[(u >> (i * 4)) & mask]
        v += temp << (i * 4)
    return v


def e_permutation(v):
    w = 0
    for i in range(0, 16):
        w += ((v >> pi_p[i]) & 1) << i
    return w


# Decrypts a ciphertext using the provided key
def decrypt_SPN(c, key):
    p = ""
    return p


print(key_gen(982832703, 1))


# 0001 0011 1010 100 1010
# 0011 1010 1001 01001