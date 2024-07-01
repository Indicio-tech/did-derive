import sys
import base58

def main():
    if len(sys.argv) < 2:
        print("USAGE: python derive.py did:key:...")
        sys.exit(1)

    did = sys.argv[1]

    _, _, multikey = did.split(":")
    multikey, _ = multikey.split("#")
    print(multikey)
    decoded = base58.b58decode(multikey[1:])
    recoded = base58.b58encode(decoded[2:])
    print(recoded.decode())


if __name__ == "__main__":
    main()
