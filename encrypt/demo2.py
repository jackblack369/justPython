from cryptography.fernet import Fernet

def encrypt(text, key):
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text.decode()

def decrypt(encrypted_text, key):
    cipher_suite = Fernet(key)
    decrypted_text = cipher_suite.decrypt(encrypted_text.encode())
    return decrypted_text.decode()

# 测试加密和解密
original_text = "Hello, World!"
encryption_key = Fernet.generate_key()

# 加密
encrypted_text = encrypt(original_text, encryption_key)
print("加密后的文本:", encrypted_text)

# 解密
decrypted_text = decrypt(encrypted_text, encryption_key)
print("解密后的文本:", decrypted_text)