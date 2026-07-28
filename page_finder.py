import argparse
import requests
from banner import banner


def scan_pages(url, wordlist):
    """
    Scan the target website using the given wordlist.
    """

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        with open(wordlist, "r") as file:
            pages = file.readlines()
    except FileNotFoundError:
        print(f"[-] Wordlist '{wordlist}' not found.")
        return

    print(f"\n[+] Target    : {url}")
    print(f"[+] Wordlist : {wordlist}")
    print("\n[+] Scanning...\n")

    for page in pages:

        page = page.strip()

        if page == "":
            continue

        full_url = f"{url.rstrip('/')}/{page}"

        try:
            response = requests.get(
                full_url,
                headers=headers,
                timeout=5
            )

            if response.status_code == 200:
                print(f"[FOUND] {full_url}")

            elif response.status_code == 403:
                print(f"[FORBIDDEN] {full_url}")

            elif response.status_code in [301, 302]:
                print(f"[REDIRECT] {full_url}")

        except requests.exceptions.RequestException:
            print(f"[ERROR] Could not connect to {full_url}")


def main():

    banner()

    parser = argparse.ArgumentParser(
        description="Simple Page Finder Tool"
    )

    parser.add_argument(
        "-u",
        "--url",
        required=True,
        help="Target URL"
    )

    parser.add_argument(
        "-w",
        "--wordlist",
        default="wordlist.txt",
        help="Wordlist file"
    )

    args = parser.parse_args()

    scan_pages(args.url, args.wordlist)


if __name__ == "__main__":
    main()
