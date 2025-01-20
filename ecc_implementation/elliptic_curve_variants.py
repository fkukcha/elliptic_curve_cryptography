# Done
# 6. Elliptic Curve Variants
# This code demonstrates the generation of ECC keys for different elliptic curve types and compares their properties.

from cryptography.hazmat.primitives.asymmetric import ec, ed25519
from cryptography.hazmat.primitives import serialization

# Generate keys for different elliptic curve types
secp256r1_key = ec.generate_private_key(ec.SECP256R1())
secp256k1_key = ec.generate_private_key(ec.SECP256K1())
ed25519_key = ed25519.Ed25519PrivateKey.generate()

# Serialize keys to PEM format
secp256r1_pem = secp256r1_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
).decode('utf-8')

secp256k1_pem = secp256k1_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
).decode('utf-8')

ed25519_pem = ed25519_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
).decode('utf-8')

# Print serialized keys
print("Elliptic Curve Variants:")
print(f"SECP256R1 key:\n{secp256r1_pem}")
print(f"SECP256K1 key:\n{secp256k1_pem}")
print(f"Ed25519 key:\n{ed25519_pem}")

# Compare properties and performance of different elliptic curve types
print("\nElliptic Curve Properties:")
print(f"SECP256R1 key size: {secp256r1_key.key_size} bits")
print(f"SECP256K1 key size: {secp256k1_key.key_size} bits")

# Get Ed25519 key size
ed25519_public_key = ed25519_key.public_key()
ed25519_key_size = len(ed25519_public_key.public_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PublicFormat.Raw
)) * 8

print(f"Ed25519 key size: {ed25519_key_size} bits")
