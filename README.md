# Page-finder-tool
## ✅ 1. Prepare your environment (correct first step) 

Before running your script, do:

```
sudo apt update
```

## 🐍 Step 2: Check Python Installation

Kali usually has Python pre-installed:

```
python3 --version
```

If not installed:

```
sudo apt install python3 -y
```
## 📄 Step 3: Create Python file

```
nano page_finder.py
```
## ✍️ Step 4: Paste this script

```
import requests

# Common pages list
paths = [
    "admin",
    "admin/login",
    "login",
    "dashboard",
    "user",
    "admin.php",
    "login.php",
    "cpanel",
    "admin/dashboard"
]

# Take input from user
url = input("Enter website URL (e.g. https://example.com): ").strip()

# Remove trailing slash
if url.endswith("/"):
    url = url[:-1]

print("\n[+] Scanning for pages...\n")

for path in paths:
    full_url = f"{url}/{path}"

    try:
        response = requests.get(full_url, timeout=5)

        if response.status_code == 200:
            print(f"[FOUND] {full_url}")
        else:
            print(f"[NOT FOUND] {full_url} (Status: {response.status_code})")

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] {full_url} - {e}")

```
## 💾 Step 5: Save and exit

- Press `CTRL + X`
- Press `Y`
- Press `Enter`
- 
## ▶️ Step 6: Run the tool

```
python3 page_finder.py
```
<img width="1032" height="127" alt="Screenshot 2026-07-08 025159" src="https://github.com/user-attachments/assets/acf342b6-c166-4e9f-a5dc-e0e4f6da2cbd" />


