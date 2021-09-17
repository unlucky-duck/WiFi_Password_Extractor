from termcolor import cprint
from itertools import cycle
from time import sleep
from sys import stdout
import subprocess
import os

loading_chars = iter(cycle('/-\|'))
colors = iter(cycle(['blue', 'red']))
os.system('cls')

print('\n Welcome to WiFi Password Extractor(written by Sina.f)\n')
sleep(.7)

for i in range(40):
    sleep(0.15)
    stdout.write(f'\r Extracting wifi passwords... {next(loading_chars)}')

sleep(1)
print('\n\n\n {:<30}|  Password\n'.format('Host name'))
output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode().split('\n')

profiles = [i.split(':')[1][1:-1] for i in output if 'All User Profile' in i]

for profile in profiles:
    result = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', profile, 'key=clear']).decode('ISO-8859-1').split('\n')
    color = next(colors)
    
    try:
        password = [b.split(':')[1][1:-1] for b in result if 'Key Content' in b][0]
        cprint(f' {profile:<30}|  {password}', color=color)
        
    except:
        cprint(f' {profile:<30}|  <No password>', color=color)
        
    sleep(.8)

figlet =  f'''\n
   _____ _                __ 
  / ____(_)              / _|
 | (___  _ _ __   __ _  | |_ 
  \___ \| | '_ \ / _` | |  _|
  ____) | | | | | (_| |_| |  
 |_____/|_|_| |_|\__,_(_)_| 
'''

for line in figlet.splitlines():
    print(line)
    sleep(.2)

sleep(1)
input(f'\n\n Press enter to exit...')
