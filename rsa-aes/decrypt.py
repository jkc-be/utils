#!/usr/bin/env python
# coding: utf-8
import os

print("installing cryptography \n")
os.system("pip install -r requirements.txt")
print("\n")

import base64
import json

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

# ### read in private pem key
print("reading in private key \n")
with open("keys/private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(), password=None, backend=default_backend()
    )

# ### read in response.json
with open("response/response.json", "r") as f:
    response = json.load(f)


# ### 1. convert base64 RSA to bytes
base64EncodedKey = response.get("base64EncodedKey", [None])[0]

EncodedKey = base64.b64decode(base64EncodedKey)


# ### 2. decrypt RSA public key to get symetric AES key
aes_key = private_key.decrypt(
    EncodedKey,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

cipher = Fernet(aes_key)

# ### 3. use AES key to decrypt message
emailEncrypted = response.get("emailEncrypted", None)
decrypted_email = cipher.decrypt(emailEncrypted).decode("utf-8")
print("encrypted email: " + emailEncrypted)
print("decrypted mail: " + decrypted_email)