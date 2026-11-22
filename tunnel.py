# tunnel.py - Multi-Device Access & Persistent Auto-Reconnecting Public Tunnel
import sys
import time
import subprocess
import re
import os

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def update_tunnel_file(url):
    try:
        with open("tunnel_url.txt", "w", encoding="utf-8") as f:
            f.write(url + "\n")
    except Exception:
        pass

def main():
    print("=" * 65)
    print("  RESEARCHMATE AI — PERSISTENT DIRECT PUBLIC TUNNEL")
    print("  Local Machine:  http://localhost:8000")
    print("  Wi-Fi Network:  http://192.168.1.5:8000 (Open on any phone/tablet/laptop)")
    print("  Connecting live public internet tunnel (Direct SSH, No Interstitial)...")
    print("=" * 65)
    sys.stdout.flush()

    cmd = [
        "ssh",
        "-o", "StrictHostKeyChecking=no",
        "-o", "ServerAliveInterval=30",
        "-o", "ServerAliveCountMax=3",
        "-R", "80:127.0.0.1:8000",
        "nokey@localhost.run"
    ]

    while True:
        try:
            print("[Tunnel] Establishing SSH connection to localhost.run relay...")
            sys.stdout.flush()
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
            for line in proc.stdout:
                line_str = line.strip()
                m = re.search(r"https://[a-zA-Z0-9\.\-_]+\.lhr\.life", line_str)
                if m:
                    url = m.group(0)
                    print("\n" + "=" * 65)
                    print(f"  [Direct Tunnel Live]: {url}")
                    print("=" * 65 + "\n")
                    update_tunnel_file(url)
                    sys.stdout.flush()
            proc.wait()
            print("[Tunnel] Relay disconnected. Reconnecting in 3s...")
            sys.stdout.flush()
        except Exception as e:
            print(f"[Tunnel] Notice ({e}), retrying in 3s...")
            sys.stdout.flush()
        time.sleep(3)

if __name__ == "__main__":
    main()
