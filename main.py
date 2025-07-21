import json
import httpx
from analyzer import guess_hash_algorithm
from hasher import verify_password


def load_config():
    with open("config.json") as f:
        return json.load(f)


def load_passwords():
    with open("passwords.txt") as f:
        return [line.strip() for line in f if line.strip()]


def send_login_request(email: str, password: str, login_url: str):
    try:
        response = httpx.post(login_url, json={"email": email, "password": password})
        print(f"\nSent login attempt. Status: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"HTTP Error: {e}")


def main():
    config = load_config()
    target_hash = config["target_hash"]
    email = config["email"]
    login_url = config["login_url"]

    passwords = load_passwords()
    method = guess_hash_algorithm(target_hash)

    print(f"Target Hash: {target_hash}")
    print(f"Guessed Method: {method}")
    print(f"Passwords to try: {len(passwords)}\n")

    for pwd in passwords:
        print(f"Trying: {pwd}")
        try:
            if verify_password(pwd, target_hash, method):
                print(f"\nMATCH FOUND: {pwd}")
                send_login_request(email, pwd, login_url)
                break
            else:
                print("No match.")
        except Exception as e:
            print(f"Error checking password: {e}")


if __name__ == "__main__":
    main()
