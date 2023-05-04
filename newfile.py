#librys   المكتبات
import os
import sys
import time
import datetime
import random
import compileall
#start
c = ['\033[1;30m','\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m','\033[1;37m']
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.02)
os.system('clear' )
os.system('clear') 
print(random.choice(c))
#__________________________________________________________________________
print ("""  
  ______   _______ ___ ___ _______ ______  
 |   _  \ |   _   |   Y   |   _   |   _  \ 
 |.  |   \|.  1___|.      |.  |   |.  |   |
 |.  |    |.  __)_|. \_/  |.  |   |.  |   |
 |:  1    |:  1   |:  |   |:  1   |:  |   |
 |::.. . /|::.. . |::.|:. |::.. . |::.|   |
 `------' `-------`--- ---`-------`--- ---'                            by : >> Black Demon                                       
""")

def main():
    print('')
    print("\033[1;31m[01] \033[36mHack with Phishing Page")
    time.sleep(0.3)
#________________
    print('\033[1;31m[02] \033[36mHack With gust ')
    time.sleep(0.3)
#__________________________________________
    print('\033[1;31m[03] \033[36mAbout ')
    time.sleep(0.3)
#_________________________________________________________________________
    print('\033[1;31m[04] \033[36mExit ')
    time.sleep(0.3)
main()
choose = input("\033[1;37mChoose an option : ")
time.sleep(0.3)

#commands

if choose ==  '1':
    os.system('bash install.sh')
    os.system('bash demon.sh')
if choose ==  '3':
    	print(''' 
Welcome To My Tool
	
Tool Dev By : >> Black Demon

My Channel : »» http://t.me/BLACK_DEMON_VX ''')

if choose == '4':
	os.system('clear')