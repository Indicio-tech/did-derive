"""Generate a seed and Indy Nym based on that seed. Follows same rules used by ACA-Py."""

from aries_askar import Key, KeyAlg
from base64 import urlsafe_b64encode
from base58 import b58encode
from secrets import token_bytes
from hashlib import sha256

from did_derive import cli, display


def main():
    cli(
        name="generate",
        description="Generate a seed and it's corresponding DID and Verkey using the same rules ACA-Py follows.",
    )

    seed = token_bytes(32)
    key = Key.from_secret_bytes(KeyAlg.ED25519, seed).get_public_bytes()
    nym1 = b58encode(key[:16]).decode()
    nym2 = b58encode(sha256(key).digest()[:16]).decode()
    verkey = b58encode(key).decode()
    short = "~" + b58encode(key[16:]).decode()

    display("Seed:", urlsafe_b64encode(seed).decode())
    display("NYM v1:", nym1)
    display("NYM v2:", nym2)
    display("Verkey:", verkey)
    display("Short Verkey:", short)


if __name__ == "__main__":
    main()
