"""
Elliptic Curve Diffie-Hellman (ECDH) key exchange implementation.
This code demonstrates the generation of private-public key pairs, scalar multiplication, and shared secret computation.
"""

import random

# Define the elliptic curve parameters (using secp256k1)
a = 0
b = 7
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
G = (55066263022277343669578718895168534326250603453777594175500187360389116729240,
     32670510020758816978083085130507043184471273380659243275938904335757337482424)
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141


def inverse_mod(k, p):
    """
    Compute the modular inverse of k modulo p.
    This function returns the unique integer x such that 0 <= x < p and (k * x) % p == 1.
    :param k: The integer to compute the modular inverse of.
    :param p: The modulus.
    :return: The modular inverse of k modulo p.
    """
    if k == 0:
        raise ZeroDivisionError('division by zero')
    if k < 0:
        return p - inverse_mod(-k, p)
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = p, k
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_s % p


def point_addition(P, Q):
    """
    Add two points P and Q on the elliptic curve.
    :param P: Point P on the elliptic curve.
    :param Q: Point Q on the elliptic curve.
    :return: The result of the point addition P + Q.
    """
    if P == (None, None):
        return Q
    if Q == (None, None):
        return P
    if P == Q:
        return point_doubling(P)
    if P[0] == Q[0] and P[1] != Q[1]:
        return (None, None)

    m = (Q[1] - P[1]) * inverse_mod(Q[0] - P[0], p) % p
    x_r = (m**2 - P[0] - Q[0]) % p
    y_r = (m * (P[0] - x_r) - P[1]) % p

    return (x_r, y_r)


def point_doubling(P):
    """
    Double a point P on the elliptic curve.
    :param P: Point P on the elliptic curve.
    :return: The result of the point doubling 2P.
    """
    if P == (None, None):
        return (None, None)

    m = (3 * P[0]**2 + a) * inverse_mod(2 * P[1], p) % p
    x_r = (m**2 - 2 * P[0]) % p
    y_r = (m * (P[0] - x_r) - P[1]) % p

    return (x_r, y_r)


def scalar_multiplication(k, P):
    """
    Perform scalar multiplication kP on the elliptic curve.
    :param k: The scalar k.
    :param P: Point P on the elliptic curve.
    :return: The result of the scalar multiplication kP.
    """
    R = (None, None)
    N = P
    while k:
        if k & 1:
            R = point_addition(R, N)
        N = point_doubling(N)
        k >>= 1
    return R


def generate_keypair():
    """
    Generate a key pair for the elliptic curve Diffie-Hellman (ECDH) key exchange.
    :return: A tuple containing the private key and the public key.
    """
    private_key = random.randint(1, n - 1)
    public_key = scalar_multiplication(private_key, G)
    return private_key, public_key


def compute_shared_secret(private_key, public_key):
    """
    Compute the shared secret for the elliptic curve Diffie-Hellman (ECDH) key exchange.
    :param private_key: Private key of the party.
    :param public_key: Public key of the other party.
    :return: Return the x-coordinate of the shared secret.
    """
    shared_secret = scalar_multiplication(private_key, public_key)
    return shared_secret[0]


if __name__ == "__main__":
    # Generate key pairs for Alice and Bob
    alice_private_key, alice_public_key = generate_keypair()
    bob_private_key, bob_public_key = generate_keypair()

    # Compute shared secrets
    alice_shared_secret = compute_shared_secret(alice_private_key, bob_public_key)
    bob_shared_secret = compute_shared_secret(bob_private_key, alice_public_key)

    # Verify that the shared secrets are equal
    # print assertions are used to ensure that the shared secrets are equal
    assert alice_shared_secret == bob_shared_secret
    print("Shared secrets match successfully.")
    print("Shared secret:", alice_shared_secret)
