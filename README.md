# elliptic_curve_cryptography

This project demonstrates various aspects of elliptic curve cryptography (ECC) using Python and the `cryptography` library. It includes implementations and comparisons of different elliptic curve operations and key generation techniques.

## Project Structure

- `ecc_implementation/`
  - `ecc_in_blockchain.py`: This script demonstrates how to generate a Bitcoin address from an ECC public key.
  - `ecdh_key_exchange.py`: Elliptic Curve Diffie-Hellman (ECDH) key exchange implementation.
  - `ecdh_key_exchange_cryptography.py`: This script demonstrates the Elliptic Curve Diffie-Hellman (ECDH) key exchange algorithm using the cryptography library.
  - `ecdsa_signature.py`: This script demonstrates how to generate an Elliptic Curve Digital Signature Algorithm (ECDSA) signature using the cryptography library.
  - `ecies_encryption.py`: Elliptic Curve Integrated Encryption Scheme (ECIES) implementation using the cryptography library.
  - `elliptic_curve_point_addition.py`: This script demonstrates the point addition operation on an elliptic curve and the reflection of the resulting point.
  - `elliptic_curve_scalar_multiplication.py`: This script demonstrates the scalar multiplication operation on an elliptic curve.
  - `elliptic_curve_variants.py`: This script demonstrates the generation of ECC key pairs for different elliptic curve types using the cryptography library.
  - `rsa_vs_ecc_key_size_comparison.py`: This script demonstrates the difference in key sizes between RSA and ECC.
  - `rsa_vs_ecc_performance_comparison.py`: This script compares the performance of RSA and ECC in terms of key generation, signing and verification.

## Requirements

- Python 3.x
- `cryptography` library
- `matplotlib` library
- `numpy` library
- `base58` library

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/fkukcha/elliptic_curve_cryptography.git
   cd elliptic_curve_cryptography
    ```
2. Install the required libraries:
   ```sh
   pip install -r requirements.txt
   ```
   
## Usage
Each script in the `ecc_implementation/` directory can be run independently. For example, to run the `ecdsa_signature.py` script, use the following command:
```sh
python ecc_implementation/ecdsa_signature.py
```


