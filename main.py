from colorama import Fore, Style
import os, getpass, platform
import nmap

PATH = os.getcwd()
USER = getpass.getuser()
HOST = platform.node()

COMMANDS = ["nmap"]

def get_cmd(user=USER, host=HOST, path=PATH):
    return f"{Fore.RED}{user}@{host} {Fore.BLUE}{path}# {Style.RESET_ALL}"

class CMDS:
    def nmap_command(target):
        nm = nmap.PortScanner()
        try:
            nm.scan(target, "22-1024")
            print(f"Scan results for {target}")

            for host in nm.all_hosts():
                print(f"Host: {host} ({nm[host].hostname()})")
                print(f"OS: {nm[host]['osmatch']}")
                for proto in nm[host].all_protocols():
                    print(f"Protocol: {proto}")
                    lport = nm[host][proto].keys()
                    for port in lport:
                        print(f"Port: {port}\tState: {nm[host][proto][port]['state']}")
        except Exception as e:
            print(f"An error occurred: {e}")           

print(f"""{Fore.RED}
░█▄█░█▀█░█░░░█▀▀░█░█░▀█░
░█░█░█▀█░█░░░█▀▀░█▀█░░█░
░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀
{Style.RESET_ALL}""")


while True:
    cmd = input(get_cmd())
    cmd_split = cmd.strip().split(" ")
    cmd_name = cmd_split[0]
    cmd_args = cmd_split[1:]
    if cmd_name.lower() in COMMANDS:
        if cmd_name.lower() == "nmap":
            CMDS.nmap_command(cmd_args[1])
    else:
        os.system(cmd)
