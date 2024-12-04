"""DID Derivation utilities."""
import argparse
from typing import Iterable
from rich.console import Console
from rich.text import Text

IMAGE_NAME = "ghcr.io/indicio-tech/did-derive:latest"

console = Console()

def cli(name: str, description: str, args: Iterable[str] | None = None):
    parser = argparse.ArgumentParser(
        prog=name,
        description=description,
    )
    for arg in args or []:
        parser.add_argument(arg)

    return parser.parse_args()


def display(label: str, text: str):
    console.print(Text(label, style="green bold"), text)
