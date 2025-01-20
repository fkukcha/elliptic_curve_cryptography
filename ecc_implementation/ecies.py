# Done
# 3. Elliptic Curve Integrated Encryption Scheme (ECIES)
# This code demonstrates how ECC can be used for secure encryption and decryption of messages.
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

# Generate ECC key pair
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

# Encrypt a message
message = b"Secret message"
shared_key = private_key.exchange(ec.ECDH(), public_key)
derived_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data'
).derive(shared_key)

iv = os.urandom(12)
cipher = Cipher(algorithms.AES(derived_key), modes.GCM(iv))
encryptor = cipher.encryptor()
ciphertext = encryptor.update(message) + encryptor.finalize()
tag = encryptor.tag

# Decrypt the message
cipher = Cipher(algorithms.AES(derived_key), modes.GCM(iv, tag))
decryptor = cipher.decryptor()
decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()

print(f"Original message: {message}")
print(f"Encrypted message: {ciphertext}")
print(f"Decrypted message: {decrypted_message}")
assert message == decrypted_message
print("Decryption successful.")
