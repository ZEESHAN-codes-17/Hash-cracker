# Python Hash Cracker

A simple, fast, and extensible hash cracker written in Python. This tool attempts to recover plaintext passwords from their hash values using a wordlist and optional word mangling (variations).

## Features
- Supports MD5, SHA1, and SHA256 hash algorithms
- Customizable wordlist support
- Simple word mangling (case changes, common suffixes, leetspeak, number appends)
- Progress reporting
- Easy to use command-line interface

## Usage

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/hash-cracker.git
cd hash-cracker
```

### 2. Prepare Your Wordlist
- By default, the tool uses `wordlist.txt` in the project directory.
- You can use your own wordlist by specifying the `-w` or `--wordlist` option.

Example `wordlist.txt`:
```
pakistan786
ilovepy123
smile
football99
admin123
qwerty!
dragonfire
sunshine22
password
letmein
```

### 3. Find the Hash to Crack
- Obtain the hash you want to crack (e.g., from a database dump or CTF challenge).
- Make sure you know the hash algorithm (MD5, SHA1, or SHA256).

### 4. Run the Cracker
```bash
python hash_cracker.py -t <target_hash> [-a <algorithm>] [-w <wordlist>] [-m]
```

#### Arguments
- `-t`, `--target` **(required)**: The hash value to crack.
- `-a`, `--algorithm`: Hash algorithm to use (`md5`, `sha1`, `sha256`). Default: `md5`.
- `-w`, `--wordlist`: Path to wordlist file. Default: `wordlist.txt`.
- `-m`, `--mangle`: Enable simple word mangling (variations).

#### Example
```bash
python hash_cracker.py -t 5f4dcc3b5aa765d61d8327deb882cf99 -a md5
```

With word mangling:
```bash
python hash_cracker.py -t 5f4dcc3b5aa765d61d8327deb882cf99 -a md5 -m
```

With a custom wordlist:
```bash
python hash_cracker.py -t <target_hash> -w /path/to/your/wordlist.txt
```

## How It Works
- Reads each word from the wordlist.
- Optionally generates variations (mangling) for each word.
- Hashes each candidate and compares it to the target hash.
- Reports the password if found, or notifies if not found after all candidates are tried.

## Example Output
```
[+] Password found: password
[+] Tried 1 candidates in 0.01 seconds
```

## Requirements
- Python 3.6 or higher (no external dependencies)

## File Structure
- `hash_cracker.py` — Main script
- `wordlist.txt` — Default wordlist (edit or replace as needed)

## License
MIT License

## Disclaimer
This tool is for educational and authorized testing purposes only. Do not use it for illegal activities.
