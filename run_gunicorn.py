import socket
import subprocess
import os


def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def main():
    port = find_free_port()
    cmd = f"gunicorn app:app -b 127.0.0.1:{port}"
    print(f"Lancement de Gunicorn sur le port: {port}")
    os.system(cmd)


if __name__ == "__main__":
    main()
