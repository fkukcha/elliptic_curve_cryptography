"""
This script demonstrates how to generate an Elliptic Curve Digital Signature Algorithm (ECDSA) signature using the
cryptography library. It generates an ECC key pair, signs a message, and verifies the signature.
"""

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

# Generate ECC key pair
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

# Sign a message
message = b"Elliptic Curve Digital Signature Algorithm"
signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

# Verify the signature
try:
    public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    print("Signature is valid.")
except:
    print("Signature is invalid.")
