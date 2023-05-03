# LFI-RCE Tool 

This is a Python tool that can be used to perform a Local File Inclusion (LFI) attack that can lead to Remote Code Execution (RCE) on a vulnerable website.

## Requirements

* Python 3.x
* requests library
* base64 library
* webbrowser library
* bs4 library

## Usage

1. Clone the repository:
```bash
git clone https://github.com/jameel3reef/mrAlphaQ.git
```
2. Navigate to the Tools directory:
```bash
cd mrAlphaQ/Tools/
```
3. Run the LFI-RCE.py script:
```bash
python LFI-RCE.py
```
4. Follow the prompts to enter the necessary information:
Ex:
```bash
python LFI-RCE.py
Enter the URL 'ex: (http://example.com/)': http://blackbox.tamuctf.com
Enter the vulnerable parameter: page
Please choose:
1- Remote Command Excution
2- PHP Info
3- Exit
Your Choice: 1
Enter a command: ls
config.php
index.php
robots.txt
sitemap.xml
static
templates
util.php
```
## Contributors
This tool was created by jameel 3reef. If you have any questions or suggestions for improvement, please feel free to contact me

## Disclaimer
This tool is provided for educational purposes only. The author is not responsible for any malicious use of this tool. Use at your own risk.
