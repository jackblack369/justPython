import base64
from cryptography.fernet import Fernet

def encrypt(text, key):
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(text.encode())
    encoded_text = base64.b64encode(encrypted_text)
    return encoded_text.decode()

def decrypt(encoded_text, key):
    cipher_suite = Fernet(key)
    decoded_text = base64.b64decode(encoded_text)
    decrypted_text = cipher_suite.decrypt(decoded_text)
    return decrypted_text.decode()

# 测试编码和加密
original_text = "Hello, World!"
encryption_key = Fernet.generate_key()

# 编码和加密
encrypted_text = encrypt(original_text, encryption_key)
print("编码和加密后的文本:", encrypted_text)

# 解码和解密
decrypted_text = decrypt(encrypted_text, encryption_key)
print("解码和解密后的文本:", decrypted_text)