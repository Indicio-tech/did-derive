"""Derive an Indy Nym from seed. Follows same rules used by ACA-Py."""

import sys
from typing import Union
from base64 import urlsafe_b64decode
from aries_askar import Key, KeyAlg
from base58 import b58encode


def validate_seed(seed: Union[str, bytes, None]) -> bytes:
    """Convert a seed parameter to standard format and check length.

    Args:
        seed: The seed to validate

    Returns:
        The validated and encoded seed

    """
    if isinstance(seed, str):
        if "=" in seed:
            seed = urlsafe_b64decode(seed)
        else:
            seed = seed.encode("ascii")
    if not isinstance(seed, bytes):
        raise ValueError("Seed value is not a string or bytes")
    if len(seed) != 32:
        raise ValueError("Seed value must be 32 bytes in length")
    return seed


def main():
    if len(sys.argv) < 2:
        print("USAGE: python from_seed.py '<seed>'")
        sys.exit(1)

    seed = sys.argv[1]

    seed = validate_seed(seed)
    key = Key.from_secret_bytes(KeyAlg.ED25519, seed).get_public_bytes()
    did = b58encode(key[:16]).decode()
    verkey = b58encode(key).decode()

    print("DID/NYM:", did)
    print("Verkey:", verkey)


if __name__ == "__main__":
    main()
