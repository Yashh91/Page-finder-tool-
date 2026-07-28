# 🔎 Page Finder

Page Finder is a Python command-line tool that helps discover common web pages and directories on a website using a wordlist. It sends HTTP GET requests to each path and displays the HTTP response status, making it useful for learning web enumeration techniques.

> **Note:** This tool is intended for educational purposes and authorized security testing only.

---

##  Features

- Discover common web pages and directories
- Custom target URL
- Custom wordlist support
- Displays HTTP response status codes
- Lightweight and easy to use
- Beginner-friendly Python code
- Cross-platform (Windows, Linux, macOS)


##  Requirements

- Python 3.8 or higher
- Requests library

##  🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Yashh91/Page-Finder.git
```

Move into the project directory:

```bash
cd Page-Finder
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---
##  Usage

Scan a website using the default wordlist:

```bash
python page_finder.py -u https://example.com
```

Use a custom wordlist:

```bash
python page_finder.py -u https://example.com -w custom_wordlist.txt
```

---

##  Example Output

```text
=========================================================
                     PAGE FINDER
---------------------------------------------------------
        Find Common Web Pages and Directories
---------------------------------------------------------
                 Developed by Yashh91
=========================================================

[+] Target    : https://example.com
[+] Wordlist  : wordlist.txt

[+] Scanning...

[FOUND] https://example.com/admin
[FOUND] https://example.com/login
[FORBIDDEN] https://example.com/dashboard
```

---

##  Screenshots

### Tool Banner

> Add your screenshot here

```
screenshots/banner.png
```

### Scan Result

> Add your screenshot here

```
screenshots/result.png
```

---

##  How It Works

1. Reads paths from the wordlist.
2. Combines each path with the target URL.
3. Sends an HTTP GET request.
4. Receives the server response.
5. Displays the HTTP status for each page.

---

##  HTTP Status Codes

| Status | Description |
|:------:|-------------|
| 200 | Page found |
| 301 | Permanent redirect |
| 302 | Temporary redirect |
| 403 | Page exists but access is forbidden |
| 404 | Page not found |

---

##  License

This project is licensed under the MIT License.

---
