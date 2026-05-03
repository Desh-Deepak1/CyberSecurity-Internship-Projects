import hashlib
import time

def generate_hash(password, algorithm='sha256'):
   """Converts password into a secure hash."""
    if algorithm == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()

def dictionary_attack(target_hash, wordlist, algorithm='sha256'):
   """Simulates dictionary attack to crack target hash."""
    print(f"\n[*] Starting Dictionary Attack using {algorithm.upper()}...")
    print(f"[*] Target Hash: {target_hash}")
    
    start_time = time.time()
    
    for word in wordlist:
      
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
    secret_password = "admin"
    print(f"Original Password: {secret_password}")
    
    stolen_hash = generate_hash(secret_password, 'sha256')
    print(f"Stolen Hash from Database: {stolen_hash}")
    
    # 2. Dictionary / Brute-force Attack Demonstration

    wordlist = [
        "123456", "password", "qwerty", "iloveyou", 
        "admin123", "root", "admin", "letmein", 
        "hacker", "codec2026"
    ]
    

    time.sleep(1)
    dictionary_attack(stolen_hash, wordlist, 'sha256')
