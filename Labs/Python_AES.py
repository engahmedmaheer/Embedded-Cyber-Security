from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data_original = b'secret data'
print(data_original)
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data_original)
print(ciphertext)
nonce = cipher.nonce


cipher = AES.new(key, AES.MODE_EAX, nonce)
data_Decrypted = cipher.decrypt_and_verify(ciphertext, tag)

print(data_Decrypted)
