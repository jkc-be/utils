#!/usr/bin/env python
# coding: utf-8
import os

print("installing cryptography \n")
os.system("pip install -r requirements.txt > /dev/null 2>&1")

import base64
import json

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet


# ### make public and private pem keypair
import subprocess
import platform
import os


def run_script():
    script_path = "keys/make.sh"

    # Convert path for Windows
    if platform.system() == "Windows":
        script_path = script_path.replace("/", "\\")
        # Assuming you have a Unix-like environment like Git Bash
        cmd = f"bash {script_path}"
    else:
        cmd = f"sh {script_path}"

    subprocess.run(cmd, shell=True)


run_script()


# ### read in pub and private key
with open("keys/private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(), password=None, backend=default_backend()
    )

with open("keys/public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read(), backend=default_backend())


# ### 1. create symetric AES key and encrypt with RSA public key
# Generate a new AES key for this encryption session
aes_key = Fernet.generate_key()
cipher = Fernet(aes_key)

# Encrypt the AES key with the RSA public key
encrypted_aes_key = public_key.encrypt(
    aes_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)


# ### 2. convert to base64
base64_encoded_key = base64.b64encode(encrypted_aes_key).decode("utf-8")


# ### 3. encrypt test email and write to response.json
# Define encryption function for data
def encrypt_value(value):
    if isinstance(value, str):
        return cipher.encrypt(value.encode()).decode()
    return None


email = "loremipsum@email.com"
email_encrypted = encrypt_value(email)

output = {
    "emailEncrypted": email_encrypted,
    "base64EncodedKey": [base64_encoded_key],
}

with open("response/response.json", "w") as f:
    json.dump(output, f)

print("\n")
print("response.json written to response/ folder")
print("\n")
print("email: " + email)
print("encrypted email: " + email_encrypted)
