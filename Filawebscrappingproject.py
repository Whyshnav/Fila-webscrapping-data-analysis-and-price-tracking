#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import libraries 

from bs4 import BeautifulSoup
import requests
from datetime import datetime,date
import time
import smtplib
import csv 


# In[ ]:


URLs = [{'a':'https://www.fila.de/en/Sneaker-color/BYB-Wmn-marshmallow-1715827.html'},{'b':'https://www.fila.de/en/Women/Streetwear/Jackets/Trilj-Puff-Jacket-teaberry-6443904.html','c':'https://www.fila.de/en/Women/Sports/Tennis/Pants/Ballpant-Bella-6315002.html'}]
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
# Open CSV file for writing
with open('f1.csv', 'a+',newline ='', encoding = 'UTF-8') as f:
    writer = csv.writer(f)
    header = ['Title','Price','Date','Time']
    writer.writerow(header)
    
    # parsing each url to find the data
    for URL in URLs:
        for key, value in URL.items():
            page = requests.get(value,headers=headers)
            soup1= BeautifulSoup(page.content,'html.parser')
            soup2 = BeautifulSoup(soup1.prettify(),'html.parser')
            
            # extracting title
            title = soup2.find(id = "productTitle").get_text().strip()
            
            # extracting price
            price = soup2.find(id= 'productPrice').get_text().strip()
            
            now = time.time()
            dt_object = datetime.fromtimestamp(now)
            
            
            # Extract the time 
            
            
            today_time = dt_object.strftime("%H:%M:%S")  
            
            # Extracting the current date
            today = date.today()
            print(title,price,today,today_time)
            
            # writing the data in csv 
            writer.writerow([title,price,today,today_time])



# In[ ]:


import pandas as pd
df = pd.read_csv(r'/Users/vaishnavkolanja/Documents/filaproject.csv')
print(df)


# In[ ]:


# checking price for each hour, here copying the same code 
def check_price():
    URLs = [{'a':'https://www.fila.de/en/Sneaker-color/BYB-Wmn-marshmallow-1715827.html'},{'b':'https://www.fila.de/en/Women/Streetwear/Jackets/Trilj-Puff-Jacket-teaberry-6443904.html','c':'https://www.fila.de/en/Women/Sports/Tennis/Pants/Ballpant-Bella-6315002.html'}]
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
    # Open CSV file for writing
    with open('f2.csv', 'a+',newline ='', encoding = 'UTF-8') as f:
        writer = csv.writer(f)
        header = ['Title','Price','Date','Time']
        writer.writerow(header)
        
        
        # parsing each url to find the data
        for URL in URLs:
            for key, value in URL.items():
                page = requests.get(value,headers=headers)
                soup1= BeautifulSoup(page.content,'html.parser')
                soup2 = BeautifulSoup(soup1.prettify(),'html.parser')
                
                
                # extracting title
                title = soup2.find(id = "productTitle").get_text().strip()
                
                # extracting price
                price= soup2.find(id= 'productPrice').get_text().strip()
                
                now = time.time()
                dt_object = datetime.fromtimestamp(now)
                
                # Extract the time
                today_time = dt_object.strftime("%H:%M:%S")
                
                # Extracting the current date
                today = date.today()
                
                #printing all data
                print(title,price,today,today_time)
                
            
                # writing the data in csv
                writer.writerow([title,price,today,today_time])
                
                # only checking price of 'a'
                if key == 'a' and price < '42 €' :
                    send_mail()
                
                


# In[ ]:


# checking value every 15 min
def main():
    while True:
        check_price()
        time.sleep(900)  # sleep for 15 minutes

if __name__ == "__main__":
    main()
    


# In[ ]:


#sending mail when price reduces certain value
def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('vkolanja@gmail.com','S@v!th@_772')
    
    subject = "The Shirt you want is below $15! Now is your chance to buy!"
    body = "Kolanja, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail('vkolanja@gmail.com',msg)
send_mail()


# In[ ]:





# In[ ]:




