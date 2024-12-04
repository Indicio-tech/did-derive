"""Default entrypoint if one isn't given."""
from rich.console import Console
from rich.text import Text

console = Console()

def main():
    # Create the help text
    help_text = Text()
    help_text.append("Available scripts:\n", style="bold underline")

    # Add script descriptions
    scripts = [
        ("generate", "generate a seed and the associated DID and verkey"),
        ("derive-did-key", "derive key material from a did:key"),
        ("from-seed", "generate a DID and verkey from a seed"),
        ("short-to-long", "convert a DID and short form verkey into a long form verkey"),
    ]

    for script, description in scripts:
        help_text.append(f"- {script}", style="bold cyan")
        help_text.append(f": {description}\n")

    # Print the help text
    console.print(help_text)
