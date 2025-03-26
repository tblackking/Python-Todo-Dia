from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Geração de chave privada RSA de 2048 bits
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Serializando a chave privada
with open("private_key.pem", "wb") as key_file:
    key_file.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ))

# Gerar e exportar a chave pública
public_key = private_key.public_key()
with open("public_key.pem", "wb") as key_file:
    key_file.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print("Chaves RSA geradas com sucesso!")
