import hashlib
import time

def generate_hash(password, algorithm='sha256'):
    """पासवर्ड को सिक्योर हैश में बदलता है"""
    if algorithm == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()

def dictionary_attack(target_hash, wordlist, algorithm='sha256'):
    """टारगेट हैश को क्रैक करने के लिए डिक्शनरी अटैक सिम्युलेट करता है"""
    print(f"\n[*] Starting Dictionary Attack using {algorithm.upper()}...")
    print(f"[*] Target Hash: {target_hash}")
    
    start_time = time.time()
    
    for word in wordlist:
        # हर शब्द को हैश करके टारगेट हैश से मिलाना
        guessed_hash = generate_hash(word, algorithm)
        
        if guessed_hash == target_hash:
            end_time = time.time()
            print(f"\n[+] SUCCESS! Password Cracked: --> {word} <--")
            print(f"[+] Time taken: {round(end_time - start_time, 4)} seconds\n")
            return word
            
    print("\n[-] FAILED: Password not found in dictionary.\n")
    return None

if __name__ == "__main__":
    print("=== Password Hashing & Cracking Tool ===")
    
    # 1. Hashing Demonstration
    secret_password = "admin" # मान लीजिए यह किसी का पासवर्ड है
    print(f"Original Password: {secret_password}")
    
    # हम SHA256 हैशिंग का इस्तेमाल कर रहे हैं
    stolen_hash = generate_hash(secret_password, 'sha256')
    print(f"Stolen Hash from Database: {stolen_hash}")
    
    # 2. Dictionary / Brute-force Attack Demonstration
    # एक छोटी सी डिक्शनरी लिस्ट (वास्तविक जीवन में यह लाखों शब्दों की फाइल होती है)
    wordlist = [
        "123456", "password", "qwerty", "iloveyou", 
        "admin123", "root", "admin", "letmein", 
        "hacker", "codec2026"
    ]
    
    # हैश को क्रैक करने की कोशिश
    time.sleep(1) # थोड़ा सस्पेंस बनाने के लिए
    dictionary_attack(stolen_hash, wordlist, 'sha256')