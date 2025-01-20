# Done
# 1. Elliptic Curve Digital Signature Algorithm (ECDSA)
# This code demonstrates how to generate an ECC key pair, sign a message using ECDSA, and verify the signature.
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
