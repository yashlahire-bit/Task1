import hashlib

def check_integrity(original_text, received_text):
    original_hash = hashlib.sha256(original_text.encode()).hexdigest()
    received_hash = hashlib.sha256(received_text.encode()).hexdigest()
    
    print(f"Original Hash: {original_hash}")
    print(f"Received Hash: {received_hash}")
    
    if original_hash == received_hash:
        print("✅ Integrity Verified: The message is safe.")
    else:
        print("❌ ALERT: Integrity Compromised! The message was changed.")

# Example
msg = "Transfer $100"
tampered = "Transfer $1000"
check_integrity(msg, tampered)
