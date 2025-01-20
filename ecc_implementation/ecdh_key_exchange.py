# Done
# 2. Elliptic Curve Diffie-Hellman (ECDH) Key Exchange
# This code demonstrates how two parties can securely exchange cryptographic keys using ECDH.
from cryptography.hazmat.primitives.asymmetric import ec

# Generate private keys for two parties
private_key_1 = ec.generate_private_key(ec.SECP256R1())
private_key_2 = ec.generate_private_key(ec.SECP256R1())

# Generate public keys
public_key_1 = private_key_1.public_key()
public_key_2 = private_key_2.public_key()

# Perform key exchange
shared_key_1 = private_key_1.exchange(ec.ECDH(), public_key_2)
shared_key_2 = private_key_2.exchange(ec.ECDH(), public_key_1)

# Verify that both shared keys are the same
assert shared_key_1 == shared_key_2
print("Shared key exchange successful.")
