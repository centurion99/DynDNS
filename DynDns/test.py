import dropbox

access_token= 'LFi5vOAIJe0AAAAAAAABwupjfsMmf5KfxeoTYaKJruwvl0NWNoKhaxj_wRG5zEjI'
client = dropbox.client.DropboxClient(access_token)

f = open('IP1.txt', 'rb')
response = client.put_file('/IP.txt', f, overwrite=True)
print ("uploaded:", response)