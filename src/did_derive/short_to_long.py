from base58 import b58encode, b58decode

from did_derive import cli, display

def main():
    args = cli(
        name="short-to-long",
        description="Turn a short form did and verkey into a long form verkey",
        args=("did", "verkey")
    )

    short = args.verkey
    if short.startswith("~"):
        short = short[1:]

    long_bytes = b58decode(args.did) + b58decode(short)
    long = b58encode(long_bytes)

    display("Long form verkey:", long.decode())


if __name__ == "__main__":
    main()
