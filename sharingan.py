from threading import Thread
import socket

def start():

    file = open("range.txt", "r")
    thread_list = []

    for line in file:

        line = line.strip().split('-')[0].split('.')
        line.pop(3)
        line = '.'.join(line)+'.'

        #geting IP from range.txt
        #192.168.0.1-192.168.0.255 to 192.168.0.

        for x in range(0, 256):

            ip = line+str(x)

            new_thread = Thread(target=check, args=(ip, ))
            thread_list.append(new_thread)
            new_thread.start()
        #create 255 threads for checking hosts

        for thread in thread_list:
            thread.join()

def check(ip):

    for port in [80, 8080, 1080]:

        try:

        #simple checking

            sock = socket.socket()
            sock.settimeout(3)
            sock.connect((ip, port))
        #if host alive
            Sharingan(sock, ip)

        except socket.timeout:

            continue

        except ConnectionRefusedError:

            pass

def Sharingan(sock, ip):

    #HTTP response for QIS_wizard.htm

    header = b"GET /QIS_wizard.htm HTTP/1.1\r\n"
    header += b"Host: "+ip.encode()+b"\r\n"
    header += b"User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0 Cyberfox/50.1.0\r\n"
    header += b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\n"
    header += b"Accept-Language: en-US,en;q=0.5\r\n"
    header += b"Accept-Encoding: gzip, deflate\r\n"
    header += b"DNT: 1\r\n"
    header += b"Connection: keep-alive\r\n"
    header += b"Upgrade-Insecure-Requests: 1\r\n\r\n"

    sock.send(header)

    try:

        response = sock.recv(1024)

        if b'HTTP/1.0 200 Ok' in response:
        	
            print('[+] %s vulnerable !' % ip)

    except ConnectionResetError:

        pass

start()
