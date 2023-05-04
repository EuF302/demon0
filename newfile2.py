#librys   المكتبات
import os
import sys
import time
import datetime
import random
import compileall
from time import sleep
import pyfiglet
from datetime import *
def stoped(y=0,m=0,d=0):
 date = datetime.now()
 if len(list(str(y))) == 4:
  if m <= 12 and m > 0:
   if d <= 31 and d > 0:
    if date.year <= y:
     if date.month <= m:
      if date.day < d:
       return True
x = stoped(2024,10,30)
if x:pass
else:quit('Stoped Tool ..!')
print("")
import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = time.asctime(t)
 
print(str);

import requests
import random
from user_agent import generate_user_agent
import pyfiglet

# = = = = = = = = = = = = 

Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح

# = = = = = = = = = = = =

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
# = = = = = = = = = = = = 
logo = pyfiglet.figlet_format('* DemOn *')
print(A+logo)
print(X+'* '*15+A)

def main():
    print('')
    print("\033[33m[\033[36m 01 \033[33m] \033[1;36mHack with Phishing Page")
    time.sleep(0.3)
# = = = = =  = = = = = = = = 
    print('\033[33m[\033[36m 02 \033[33m] \033[1;36mHack With guess ')
    time.sleep(0.3)
# = = = = = = = = = = = = = 
    print('\033[33m[\033[36m 03 \033[33m] \033[1;36mAbout ')
    time.sleep(0.3)
# = = = = = = = = = = = = = = = = = = = = = = 
    print('\033[33m[\033[36m 04 \033[33m] \033[1;36mExit ')
    time.sleep(0.3)
main()
choose = input("\033[33mChoose an option :\033[36m  ")
time.sleep(0.3)

#commands

# = = = = = = = = = = = = = = = = = = = = = = 

if choose ==  '1':
    os.system('bash install.sh')
    os.system('bash demon.sh')
# = = = = = = = = = = = = = = = = = = 
if choose == '2':
		os.system('python instach.py')
# = = = = = = = = = = = = = = = = = = 

if choose ==  '3':
    	print('''
\033[35mWelcome To My Tool
	
\033[33mTool Dev By : >> \033[31mBlack Demon

\033[37mMy Channel : »» \033[34mhttp://t.me/BLACK_DEMON_VX ''')

# = = = = = = = = = = = = = = = = = = 

if choose == '4':
	os.system('clear')