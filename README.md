# DID Derivation Tools

This repo is a collection of DID Derivation tools.

## Using the Docker Image

```sh
docker run --rm -it ghcr.io/indicio-tech/did-derive:latest SCRIPT PARAMETERS...
```

Be sure to update your local image periodically:

```sh
docker pull ghcr.io/indicio-tech/did-derive:latest
```

### Available Scripts

- `generate`: generate a seed and the associated DID and verkey
- `derive-did-key`: derive key material from a did:key
- `from-seed`: generate a DID and verkey from a seed
- `short-to-long`: convert a DID and short form verkey into a long form verkey

### Generate a new seed

This will generate a new seed and display the associated did/nym and verkey.

```sh
docker run --rm -it ghcr.io/indicio-tech/did-derive:latest generate
```

## Convert short form verkey to long form

This will take a did and short form verkey and turn it into the long form verkey

```sh
docker run --rm -it ghcr.io/indicio-tech/did-derive:latest short-to-long <did> <short>
```

## Derive an Indy Nym/DID from a Seed

This derivation process follows the same rules ACA-Py follows when deriving a DID from a seed.

```sh
docker run --rm -it ghcr.io/indicio-tech/did-derive:latest from-seed '<seed>'
```

## Derive key from did:key

```sh
docker run --rm -it ghcr.io/indicio-tech/did-derive:latest derive-did-key 'did:key:...'
```

First value printed is the multikey. The second value is the decoded key in base58 representation.

The second value is the key to use in the configuration.
