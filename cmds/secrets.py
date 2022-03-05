#!/usr/local/bin/python
import gnupg
import base64

def encode(data):
    return base64.b64encode(data.encode('ascii')).decode('ascii')

def decode(data):
    return base64.b64decode(data.encode('ascii')).decode('ascii')

def import_key(gpg, key_path):
    key = open(key_path, 'r').read()
    fingerprint = gpg.import_keys(key).fingerprints[0]
    gpg.trust_keys(fingerprint, 'TRUST_ULTIMATE')

    return fingerprint

def encrypt(public_key_path, data):
    gpg = gnupg.GPG()
    fingerprint = import_key(gpg, public_key_path)

    return encode(str(gpg.encrypt(data, fingerprint)))

def decrypt(private_key_path, data):
    gpg = gnupg.GPG()
    fingerprint = import_key(gpg, private_key_path)

    result = str(gpg.decrypt(decode(data)))

    gpg.delete_keys(fingerprint, True, expect_passphrase=False)

    return result
