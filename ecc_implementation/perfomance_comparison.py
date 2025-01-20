# Done
# 4. Performance Comparison
# This code compares the performance of ECC with RSA in terms of key generation, signing and verification times.

import time
from cryptography.hazmat.primitives.asymmetric import rsa, ec, padding
from cryptography.hazmat.primitives import hashes

# RSA key generation
start_time = time.time()
rsa_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
rsa_key_gen_time = time.time() - start_time

# ECC key generation
start_time = time.time()
ecc_key = ec.generate_private_key(ec.SECP256R1())
ecc_key_gen_time = time.time() - start_time

# RSA signing
message = b"Performance comparison"
start_time = time.time()
rsa_signature = rsa_key.sign(message, padding.PKCS1v15(), hashes.SHA256())
rsa_sign_time = time.time() - start_time

# ECC signing
start_time = time.time()
ecc_signature = ecc_key.sign(message, ec.ECDSA(hashes.SHA256()))
ecc_sign_time = time.time() - start_time

# RSA verification
start_time = time.time()
rsa_key.public_key().verify(rsa_signature, message, padding.PKCS1v15(), hashes.SHA256())
rsa_verify_time = time.time() - start_time

# ECC verification
start_time = time.time()
ecc_key.public_key().verify(ecc_signature, message, ec.ECDSA(hashes.SHA256()))
ecc_verify_time = time.time() - start_time

print(f"RSA key generation time: {rsa_key_gen_time:.6f} seconds")
print(f"ECC key generation time: {ecc_key_gen_time:.6f} seconds")
print()
print(f"RSA signing time: {rsa_sign_time:.6f} seconds")
print(f"ECC signing time: {ecc_sign_time:.6f} seconds")
print()
print(f"RSA verification time: {rsa_verify_time:.6f} seconds")
print(f"ECC verification time: {ecc_verify_time:.6f} seconds")
