import urllib.request
import time
import dropbox
#print (urllib.request.urlopen("http://checkip.dyndns.com").read())

 
def getip():
    try:
        html=urllib.request.urlopen("http://checkip.dyndns.com").read().decode()
        iphtm=html.split()[-1]
        ip=iphtm[0:-14]
        #print(ip)
    except:
        print("No Connection!")
        return "0"
    return ip
    
def main():
    globalip=getip()
    while(True):
        time.sleep(5000)
        ip=getip()
        if ip is not globalip:
            globalip=ip
            #send
        else:
            pass
            
            
            
 
#main()