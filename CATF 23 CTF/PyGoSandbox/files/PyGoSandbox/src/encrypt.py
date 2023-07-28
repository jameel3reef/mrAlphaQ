import hashlib
from os import getenv
from rich.console import Console

meow = Console()
def EncryptFlag():
	# MEOW
	flag =  getenv("FLAG")
	digest = hashlib.sha256(flag.encode()).hexdigest()
	meow.print(f"[white]Encrypted Flag[/white]: [blue]{digest}[/blue]")
