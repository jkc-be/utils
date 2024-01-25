#!bin.bash
openssl genpkey -algorithm RSA -out keys/private_key.pem -pkeyopt rsa_keygen_bits:4096

openssl rsa -pubout -in keys/private_key.pem -out keys/public_key.pem
