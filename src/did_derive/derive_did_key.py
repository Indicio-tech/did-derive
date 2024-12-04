import base58

from did_derive import cli, display

def main():
    args = cli(
        name="derive-key",
        description="Display the base58 encoded key derived from a did:key",
        args=("did",)
    )

    _, _, multikey = args.did.split(":")
    multikey, _ = multikey.split("#")
    display("multikey:", multikey)
    decoded = base58.b58decode(multikey[1:])
    recoded = base58.b58encode(decoded[2:])
    display("base58:", recoded.decode())


if __name__ == "__main__":
    main()
