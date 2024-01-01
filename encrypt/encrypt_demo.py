import binascii
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# RSA 秘钥公钥初始化

# RSA 密钥生成
private_key = rsa.generate_private_key(
    public_exponent=65537, key_size=512, backend=default_backend()
)
public_key = private_key.public_key()


if __name__ == "__main__":
    # 秘钥序列化内容
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    private_key_content = private_key_pem.decode("utf-8")
    public_key_content = public_key_pem.decode("utf-8")
    print(f"private_key: {private_key_content} \n public_key: {public_key_content}")
    # 加密
    message = b"hello world"
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    ciphertext_hex_content = binascii.hexlify(ciphertext).decode()
    print(f"ciphertext: {ciphertext_hex_content}")

    # ciphertext_hex_content 转为 bytes
    ciphertext = binascii.unhexlify(ciphertext_hex_content)

    # 解密
    decrypted_message = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    decrypted_message_content = decrypted_message.decode()
    print(f"decrypted_message: {decrypted_message_content}")