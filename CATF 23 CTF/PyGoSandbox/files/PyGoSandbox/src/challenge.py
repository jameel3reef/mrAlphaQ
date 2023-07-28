import subprocess
from rich.console import Console
import sys
sys.tracebacklimit = 0

meow = Console()

def GoRunner():
    try:
        BLOCKLIST = ["Scan","os","net","exec","syscall","cli","bufio","Flag","chatgpt"]
        meow.print("[bold white][+] Welcome to the safest Golang Sandbox compiler in the wild!...[/bold white]")
        meow.print("[green]\[🐱] Meow your Go code Below Ending with 'EOF' (Spam enter to finish):[/green]")
        go_code = ""
        while True:
            line = input()
            if line == "EOF":
                break
            go_code += line + "\n"
        
        if any([b in go_code for b in BLOCKLIST]):
            meow.print("[bold red]\[!] Hacker Detected!![/bold red]")
            exit(2)
        with open('temp.go', 'w') as file:
            file.write(go_code)

        run_code = subprocess.Popen(['go', 'run','temp.go'],stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        run_code, compile_error = run_code.communicate()
        meow.print(run_code.decode())
        subprocess.run(['rm', 'temp.go'])
    except Exception:
        pass


def EncryptFlag():
    from encrypt import EncryptFlag
    EncryptFlag()
    

def main():
    try:
        GoRunner()
        EncryptFlag()
    except Exception:
        pass

main()
