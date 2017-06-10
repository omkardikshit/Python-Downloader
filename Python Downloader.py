import urllib.request
import random

x = input(r"Enter Link Of Thing : ")
y = input(r"Enter The Name Of Thing : ")
z = input(r"Write The Extension : ")
a = input(r"Write its Adress : ")

def download_web_image(url):      
   name = y      
   full_name = str(a+ name) + z      
   urllib.request.urlretrieve(url,full_name)

download_web_image (x)   
