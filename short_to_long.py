import sys
from base58 import b58encode, b58decode

def main():
    if len(sys.argv) < 3:
        print("USAGE: python short_to_long.py <did> <short verkey>")
        sys.exit(1)

    did = sys.argv[1]
    short = sys.argv[2]
    if short.startswith("~"):
        short = short[1:]

    long_bytes = b58decode(did) + b58decode(short)
    long = b58encode(long_bytes)

    print("Long form verkey:", long.decode())


if __name__ == "__main__":
    main()
