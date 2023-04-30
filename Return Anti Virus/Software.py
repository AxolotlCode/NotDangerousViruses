import time
import random
import mouse

ALRInstalled = input('Have You Already Installed Return Antivirus?: ')

if ALRInstalled == "No":
    time.sleep(1)
    print('Welcome To The Return Antivirus Installer')
    print('The Worlds Most Compact Antivirus (sure)')
    time.sleep(3)
    print('Installing To C Drive')
    print('Installing...')
    time.sleep(2)
    print('Done!')
else:
    print('Running Beginning Virus Scan')
    time.sleep(11)
    print('25 Viruses Found')
    time.sleep(2)
    print('Terminating Viruses...')
    time.sleep(2)
    #Payload Goes Here
    for i in range(101):
        mouse.move(100, 0, absolute=False, duration=0.1)