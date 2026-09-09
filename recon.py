import sys
import socket

SUBS = ["www", "mail", "admin", "dev", "vpn", "portal", "api", "staging"]

def main(domain):
    for s in SUBS:
        host = f"{s}.{domain}"
        try:
            print(f"[+] {host} -> {socket.gethostbyname(host)}")
        except socket.gaierror:
            pass

if __name__ == "__main__":
    main(sys.argv[1])