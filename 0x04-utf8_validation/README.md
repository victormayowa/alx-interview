Toggle navigation
Curriculum
Short Specializations
Average: 89.53%
0x04. UTF-8 Validation
Algorithm
Python
 By: Carrie Ybay, Software Engineer at Holberton School
 Weight: 1
 Project will start Jan 29, 2024 6:00 AM, must end by Feb 2, 2024 6:00 AM
 Checker will be released at Jan 30, 2024 6:00 AM
 An auto review will be launched at the deadline
Resources
Read or watch:

UTF-8
Characters, Symbols, and the Unicode Miracle
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7.x)
All your files must be executable
Tasks
0. UTF-8 Validation
mandatory
Write a method that determines if a given data set represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
carrie@ubuntu:~/0x04-utf8_validation$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

carrie@ubuntu:~/0x04-utf8_validation$
carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
carrie@ubuntu:~/0x04-utf8_validation$
Repo:

GitHub repository: alx-interview
Directory: 0x04-utf8_validation
File: 0-validate_utf8.py
 
Copyright © 2024 ALX, All rights reserved.

To properly cite a webpage using the APA (American Psychological Association) style, you can follow the following format:


Author(s). (Date). Title of the page. Site Name. Retrieved from URL


For example, suppose you want to cite a webpage about climate change from the Environmental Protection Agency website, with no specific author or publication date listed. The citation would look like this:


Environmental Protection Agency. (n.d.). Climate Change. Retrieved from https://www.epa.gov/climate-change


Please note that in this example, since there is no specific author mentioned, the organization or website name is used in the author's place. Additionally, if there is a specific publication date available, it should be included in the format (Author(s), Date).
