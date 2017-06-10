import urllib.request
#imports The Url Library for downloadig from web

x = input(r"Enter Link Of Thing : ")#A variable that allows user to enter the link
y = input(r"Enter The Name Of Thing : ")# A variable that allows user to enter file name
z = input(r"Write The Extension : ")# A variable that allows user to type its extension
a = input(r"Write its Adress : ")# A Variable that allows to write its address

def download_web_image(url):      
   name = y  # name of the file    
   full_name = str(a+ name) + z    # its full name like (C:\Users\Admin\Desktop\Red.png)  
   urllib.request.urlretrieve(url,full_name)# requests to web to do so 

download_web_image (x)   
