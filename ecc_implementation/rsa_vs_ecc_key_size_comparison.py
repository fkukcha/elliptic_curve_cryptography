"""
This script demonstrates the difference in key sizes between RSA and ECC.
It generates a 2048-bit RSA key pair and a 256-bit ECC key pair and compares their sizes.
"""

from cryptography.hazmat.primitives.asymmetric import rsa, ec
from cryptography.hazmat.primitives import serialization

# Generate RSA key pair
rsa_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Generate ECC key pair
ecc_key = ec.generate_private_key(
    ec.SECP256R1()
)

# Serialize keys to get their sizes
rsa_private_key_bytes = rsa_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

ecc_private_key_bytes = ecc_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

# Print key sizes
print(f"RSA 2048-bit private key size: {len(rsa_private_key_bytes)} bytes")
print(f"ECC 256-bit private key size: {len(ecc_private_key_bytes)} bytes")

# Security comparison
print("\nSecurity Comparison:")
print("RSA 2048-bit key provides approximately 112 bits of security.")
print("ECC 256-bit key provides approximately 128 bits of security.")
