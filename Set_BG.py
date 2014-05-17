import subprocess, time
subprocess.call(['bg.py'], shell=True, creationflags=subprocess.SW_HIDE)
print("Downloaded.")

subprocess.call(['bg.bat'], shell=True, creationflags=subprocess.SW_HIDE)
print("Set BG")

while 1:
    subprocess.call(['update1.bat'], shell=True, creationflags=subprocess.SW_HIDE)
    print('update')
