"""Derive an Indy Nym from seed. Follows same rules used by ACA-Py."""

from aries_askar import Key, KeyAlg
from base64 import urlsafe_b64encode
from base58 import b58encode
from secrets import token_bytes
from hashlib import sha256


def main():
    seed = token_bytes(32)
    key = Key.from_secret_bytes(KeyAlg.ED25519, seed).get_public_bytes()
    nym1 = b58encode(key[:16]).decode()
    nym2 = b58encode(sha256(key).digest()[:16]).decode()
    verkey = b58encode(key).decode()

    print("Seed:", urlsafe_b64encode(seed).decode())
    print("NYM v1:", nym1)
    print("NYM v2:", nym2)
    print("Verkey:", verkey)


if __name__ == "__main__":
    main()
