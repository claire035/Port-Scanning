####################
#https://t.me/ClairePython
####################
import socket
import sys
import os
import time
import socket
import random
from datetime import datetime
import requests,os,names,random,time,mechanize,sys
import requests,random,mechanize,datetime

Z = '\033[1;31m' #احمر
F = '\033[2;32m' #اخضر.
#
import os
import sys
import time
#import pyfiglet,datetime,webbrowser
import os
from time import *
from time import sleep
#from datatime import datatime
os.system("clear")
os.system("figlet C L A I R E")
print(' ')
print ('\033[1;31m')
print ("========================================")
print ('\033[1;32m')
print ("insta    : https://instagram.com/rssae.1 ")
print ("github   : https://github.com/claire035")
print ("telegram : https://t.me/ClairePython ")
print('')
print ("========================================")
print ('\033[1;33m')
ip=input(F+'==> Enter Ip To Start ==> :')
t2 = datetime.datetime.today()
print(F+'Scanning Start... %s Plase Wait..'%ip)
sleep(1)
########################
try:
        for port in range(1, 6553):
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                if(s.connect_ex((ip,port))==0):
                        try:
                                serv=socket.getservbyport(port)
                        except:
                                serv=F+'Unknow Service'
                        print(Z+'Port %s Open Service: %s ' %(port,serv))
               # t1 = datetime.datetime.today()
              #  t3=t1-t2
        print(F+'Scanning Completed on %s'+ip)
except KeyboardInterrupt:
        print(F+'See You Soon. .....')
########################
