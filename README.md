# Derive key from did:key

## Setup

```sh
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Run

```sh
# Ensure environment is active
python derive.py 'did:key:....'
```

First value printed is the multikey. The second value is the decoded key in base58 representation.

The second value is the key to use in the configuration.
