# DID Derivation Tools

This repo is a collection of DID Derivation tools.

## Setup

```sh
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Generate a new seed

This will generate a new seed and display the associated did/nym and verkey.

```sh
# Ensure environment is active (see setup)
python generate.py
```

## Convert short form verkey to long form

This will take a did and short form verkey and turn it into the long form verkey

```sh
# Ensure environment is active (see setup)
python short_to_long.py <did> <short>
```

## Derive an Indy Nym/DID from a Seed

This derivation process follows the same rules ACA-Py follows when deriving a DID from a seed.

```sh
# Ensure environment is active (see setup)
python from_seed.py '<seed>'
```

## Derive key from did:key

```sh
# Ensure environment is active
python derive.py 'did:key:....'
```

First value printed is the multikey. The second value is the decoded key in base58 representation.

The second value is the key to use in the configuration.
