# Password Hash Verification Educational Tool

This educational project demonstrates how password hashing and verification works in cybersecurity. It includes hash algorithm detection, password verification, and basic HTTP authentication testing.

## Project Structure

```
FastAPIProject/
├── main.py          # Main execution script
├── analyzer.py      # Hash algorithm detection
├── hasher.py        # Password hashing and verification
├── config.json      # Configuration file
├── passwords.txt    # Test passwords list
├── requirements.txt # Python dependencies
└── test_main.http   # HTTP test file
```

## Components

### 1. Hash Algorithm Analyzer (`analyzer.py`)

The `guess_hash_algorithm()` function identifies hash types by examining their format:

- **bcrypt**: Starts with `$2a$`, `$2b$`, or `$2y$`
- **argon2**: Starts with `$argon2`
- **pbkdf2**: Starts with `$pbkdf2`
- **SHA256**: 64-character hexadecimal string
- **SHA512**: 128-character hexadecimal string
- **MD5**: 32-character hexadecimal string

### 2. Password Hasher (`hasher.py`)

Uses the `passlib` library to handle multiple hashing schemes:

- **`hash_password()`**: Creates hashes using specified methods
- **`verify_password()`**: Verifies plaintext passwords against hashes
- Supports bcrypt, argon2, and sha256_crypt algorithms

### 3. Configuration (`config.json`)

Contains the testing parameters:

```json
{
  "target_hash": "$2b$12$...",  // The hash to match against
  "_comment": "This target_hash is considered the password stored in database",
  "login_url": "http://localhost:8000/login",  // Test endpoint
  "email": "admin@example.com"  // Test email
}
```

### 4. Password List (`passwords.txt`)

Contains common passwords for testing:
- 123456
- password
- admin123
- s3cr3t123
- letmein

## How It Works

1. **Load Configuration**: Reads target hash, email, and login URL from `config.json`

2. **Load Password List**: Reads potential passwords from `passwords.txt`

3. **Hash Algorithm Detection**: Uses pattern matching to identify the hash type (bcrypt, argon2, etc.)

4. **Password Testing Loop**: 
   - Tries each password from the list
   - Verifies if the password matches the target hash
   - Stops when a match is found

5. **HTTP Authentication Test**: 
   - When a match is found, attempts to login via HTTP POST
   - Sends JSON payload: `{"email": "admin@example.com", "password": "matched_password"}`

## Example Output

```
Target Hash: $2b$12$rRsaetziH8FLX6TlGhwJpOHnopQsTgS.86ieVt8b5MVCmL1TO4aBe
Guessed Method: bcrypt
Passwords to try: 5

Trying: 123456
No match.
Trying: password

MATCH FOUND: password
HTTP Error: [Errno 61] Connection refused
```

## Dependencies

Install required packages:
```bash
pip install -r requirements.txt
```

Main dependencies:
- `passlib`: Password hashing library
- `httpx`: HTTP client for authentication testing

## Running the Tool

  - pip install -r requirements.txt
  - python main.py
  - python3 main.py
  - python -u main.py
  - python main.py > output.log 2>&1


### Basic Usage

```bash
# Install dependencies first
pip install -r requirements.txt

# Run the password verification tool
python main.py
```

### Alternative Commands

```bash
# Run with Python 3 explicitly
python3 main.py

# Run in verbose mode (if your terminal supports it)
python -u main.py

# Run and save output to file
python main.py > output.log 2>&1
```

### What the Script Does

The script will automatically:
1. Analyze the target hash format
2. Test each password in the list
3. Report any matches found
4. Attempt HTTP authentication if a match is discovered
