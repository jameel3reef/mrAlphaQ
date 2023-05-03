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
`git clone https://github.com/jameel3reef/mrAlphaQ.git`
2. Navigate to the Tools directory:
`cd mrAlphaQ/Tools/`
3. Run the LFI-RCE.py script:
`python LFI-RCE.py`
4. Follow the prompts to enter the necessary information:
Ex:
```bash
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

