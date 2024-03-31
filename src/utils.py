import hashlib


def generate_hash(url: str) -> str:
    # Encode the URL as bytes
    url_bytes = url.encode("utf-8")
    print(url_bytes)
    # Generate SHA-256 hash
    sha256_hash_url = hashlib.sha256(url_bytes).hexdigest()

    return sha256_hash_url
