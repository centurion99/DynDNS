from retrieveip import getip
from gui import guir
import dropbox
import time
import _thread


print("Hallo!")

access_token= 'LFi5vOAIJe0AAAAAAAABwupjfsMmf5KfxeoTYaKJruwvl0NWNoKhaxj_wRG5zEjI'
client = dropbox.client.DropboxClient(access_token)
#print ('linked account: ', client.account_info())
ip=getip()
f = open("IP1.txt","w")
f.write(ip)
f.close()
f = open('IP1.txt', 'rb')
response = client.put_file('/IP.txt', f, overwrite=True)
print ("uploaded:", response)


_thread.start_new_thread(guir, (ip,))  

  
    
while 1:
    f = open("IP1.txt","r")
    ip=f.read()
    f.close()
    #print("IP ist:", ip)
    #print("getip:", getip())
    
    newip=getip()
    if ip == newip:
        print("IP gleich")
        #var.set("Test")
        print ("Start : %s" % time.ctime()) 
          
    else:
        f = open("IP1.txt","w")
        f.write(newip)
        f.close()
        
        f = open('IP1.txt', 'rb')
        try:
            response = client.put_file('/IP.txt', f, overwrite=True)
        except:
            print("not uploaded")
        print ("uploaded:", response)
    

    
    time.sleep(10)



#flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
#app_key = '7wzi5o2lcot00cc'
#app_secret = 'wsbkbmnp6w3qamc'

#authorize_url = flow.start()
#print ('1. Go to: ' + authorize_url)
#print ('2. Click "Allow" (you might have to log in first)')
#print ('3. Copy the authorization code.')

#code = 'LFi5vOAIJe0AAAAAAAABvW6NxODT5A3bOtUUPz4vgNw'
#code = input("Enter the authorization code here: ").strip()

#access_token, user_id = flow.finish(code)