#!/usr/bin/env python3
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os
import socket
import webbrowser

ROOT = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PREFERRED_PORT = 8000

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

def find_port(start: int) -> int:
    for port in range(start, start + 50):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind((HOST, port))
                return port
            except OSError:
                continue
    raise RuntimeError("No free local preview port found from 8000 to 8049.")

if __name__ == "__main__":
    os.chdir(ROOT)
    port = find_port(PREFERRED_PORT)
    url = f"http://{HOST}:{port}/"
    print(f"ArkFlame Studios local preview: {url}")
    print("Press Ctrl+C to stop.")
    webbrowser.open(url)
    ThreadingHTTPServer((HOST, port), Handler).serve_forever()
