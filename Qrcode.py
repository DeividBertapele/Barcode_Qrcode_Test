from os import link
import qrcode 

link = 'https://github.com/'
img = qrcode.make(link) 
img.save('MyQRCode_GitHub.png')