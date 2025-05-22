from cryptography.hazmat.primitives import serialization

# Cargar clave privada
with open("private.pem", "rb") as f:
    clave_privada = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

# Firmar token con RS256
token_rsa = jwt.encode(
    payload,
    clave_privada,
    algorithm="RS256"
)