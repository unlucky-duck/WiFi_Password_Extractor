from itertools import cycle
from time import sleep
from sys import stdout
import subprocess
import os

os.system('cls')
chars = iter(cycle('/-\|'))

print('\n Welcome to WiFi Password Extractor(written by Sina.f)\n')
sleep(.7)

for profile in range(40):
    sleep(0.15)
    stdout.write(f'\r Extracting wifi passwords... {next(chars)}')

sleep(1)
print('\n\n\n {:<30}|  Password\n'.format('Host name'))
output = subprocess.check_output(
    ['netsh', 'wlan', 'show', 'profiles']).decode().split('\n')

profiles = [i.split(':')[1][1:-1] for i in output if 'All User Profile' in i]

for profile in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', 
                                       profile, 'key=clear']).decode().split('\n')
    
    password = [b.split(':')[1][1:-1] for b in results if 'Key Content' in b][0]
    
    if password:
        print(f' {profile:<30}|  {password}')
        
    else:
        print(f' {profile:<30}|  ""')
        
    sleep(.8)
        
input('\n Press enter to exit...')
