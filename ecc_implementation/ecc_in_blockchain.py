# Should be integrated in TeXStudio
# 5. Elliptic Curve Cryptography in Blockchain
# This code demonstrates the use of ECC in blockchain technologies by generating a Bitcoin address.

import hashlib
import base58
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# Generate ECC key pair
private_key = ec.generate_private_key(ec.SECP256K1())
public_key = private_key.public_key()

# Serialize public key
public_key_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.X962,
    format=serialization.PublicFormat.UncompressedPoint
)

# Perform SHA-256 and RIPEMD-160 hashing
sha256_hash = hashlib.sha256(public_key_bytes).digest()
ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()

# Add version byte (0x00 for mainnet)
versioned_payload = b'\x00' + ripemd160_hash

# Perform double SHA-256 hashing for checksum
checksum = hashlib.sha256(hashlib.sha256(versioned_payload).digest()).digest()[:4]

# Create the final Bitcoin address
address_bytes = versioned_payload + checksum
bitcoin_address = base58.b58encode(address_bytes)

print(f"Bitcoin address: {bitcoin_address.decode()}")
