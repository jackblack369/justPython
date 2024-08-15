import hashlib

def generate_sha256_hash(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()

# 示例用法
data = "Hello, World!"
sha256_hash = generate_sha256_hash(data)
print("SHA-256 Hash:", sha256_hash)