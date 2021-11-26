import os, socket, threading, concurrent.futures, colorama, webbrowser
from colorama import Fore
colorama.init()

webbrowser.open_new_tab("https://discord.gg/yrcAqymE5M")
os.system(f"title Created By Solo!")

LIGHT_RED = Fore.LIGHTRED_EX
LIGHT_CYAN = Fore.LIGHTCYAN_EX
LIGHT_GREEN = Fore.LIGHTGREEN_EX

print_lock = threading.Lock()
print(LIGHT_RED)
print("""
███████╗ ██████╗ ██╗      ██████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔════╝██╔═══██╗██║     ██╔═══██╗    ██╔════╝██╔════╝██╔══██╗████╗  ██║
███████╗██║   ██║██║     ██║   ██║    ███████╗██║     ███████║██╔██╗ ██║
╚════██║██║   ██║██║     ██║   ██║    ╚════██║██║     ██╔══██║██║╚██╗██║
███████║╚██████╔╝███████╗╚██████╔╝    ███████║╚██████╗██║  ██║██║ ╚████║
╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝""")
print(LIGHT_RED)
ip = input("Enter IP/HOST: ")

def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print(LIGHT_GREEN + f"[{port}]" + LIGHT_CYAN + " Open!")
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(1000):
        executor.submit(scan, ip, port + 1)
print(LIGHT_RED)
print("Scanned All Possible Ports!")
os.system("pause >nul")
