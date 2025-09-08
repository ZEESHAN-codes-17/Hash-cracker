import hashlib
import argparse
import sys
import time
import os

# -------- Compute hash for a given word --------
def compute_hash(word: str, algorithm: str) -> str:
    word_bytes = word.encode("utf-8")
    if algorithm == "md5":
        return hashlib.md5(word_bytes).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(word_bytes).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(word_bytes).hexdigest()
    else:
        raise ValueError("Unsupported algorithm. Use md5, sha1, or sha256.")

# -------- Generate simple variations of a word --------
def word_variations(word: str, max_append: int = 100):
    yield word
    yield word.lower()
    yield word.upper()
    yield word.capitalize()
    yield word.title()

    # common suffixes
    for suffix in ["123", "!", "2025"]:
        yield word + suffix

    # small number appends
    for n in range(max_append):
        yield word + str(n)

    # basic leetspeak
    replacements = {
        "a": "@",
        "o": "0",
        "i": "1",
        "e": "3",
        "s": "5"
    }
    for k, v in replacements.items():
        if k in word.lower():
            yield word.replace(k, v)
            yield word.replace(k.upper(), v)

# -------- Load wordlist --------
def load_wordlist(path: str):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                word = line.strip()
                if word:
                    yield word
    except FileNotFoundError:
        print(f"[!] Wordlist file not found: {path}")
        sys.exit(1)

# -------- Main cracking function --------
def crack_hash(target_hash: str, algorithm: str, wordlist_path: str, mangle: bool = False):
    start = time.time()
    tried = 0

    for word in load_wordlist(wordlist_path):
        candidates = word_variations(word) if mangle else [word]

        for candidate in candidates:
            tried += 1
            hashed = compute_hash(candidate, algorithm)

            if hashed == target_hash.lower():
                elapsed = time.time() - start
                print(f"\n[+] Password found: {candidate}")
                print(f"[+] Tried {tried} candidates in {elapsed:.2f} seconds")
                return

            # Print progress every 1000 tries
            if tried % 1000 == 0:
                print(f"[-] Tried {tried} candidates so far...")

    elapsed = time.time() - start
    print(f"\n[-] Password not found in wordlist.")
    print(f"[-] Tried {tried} candidates in {elapsed:.2f} seconds")

# -------- CLI Parser --------
def parse_args():
    parser = argparse.ArgumentParser(description="Simple Python Hash Cracker")
    parser.add_argument("-t", "--target", required=True, help="Target hash to crack")
    parser.add_argument("-a", "--algorithm", choices=["md5", "sha1", "sha256"], default="md5", help="Hash algorithm (default: md5)")
    parser.add_argument("-w", "--wordlist", default="wordlist.txt", help="Path to wordlist file (default: wordlist.txt)")
    parser.add_argument("-m", "--mangle", action="store_true", help="Enable simple word mangling (variations)")
    return parser.parse_args()

# -------- Main entry point --------
def main():
    args = parse_args()
    crack_hash(args.target, args.algorithm, args.wordlist, args.mangle)

if __name__ == "__main__":
    main()
