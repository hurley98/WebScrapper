import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.emag.ro/noapte-nesfarsita-agatha-christie-9786063343780/pd/D6TTBGBBM/?X-Search-Id=172fca057784e82ed6c2&X-Product-Id=6077496&X-Search-Page=1&X-Search-Position=0&X-Section=search&X-MB=0&X-Search-Action=view'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

def check_price():
        
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(attrs={"page-title"}).get_text()
    price = soup.find(attrs={"product-new-price"}).get_text()
    new_price = price.strip()
    converted_price = float(new_price[0:2])

    if(converted_price < 30.0):
        send_email()

    ##print(title.strip())
    print(converted_price)

    if(converted_price < 20.0):
        send_email()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() ##verification message
    server.starttls() ##establishes connection
    server.ehlo()

    server.login('alex.costanza98@gmail.com', 'qjvksmgskfaqgepc')

    subject = 'Pretul e scazut!'
    body = 'Verifica link-ul EMAG https://www.emag.ro/noapte-nesfarsita-agatha-christie-9786063343780/pd/D6TTBGBBM/?X-Search-Id=172fca057784e82ed6c2&X-Product-Id=6077496&X-Search-Page=1&X-Search-Position=0&X-Section=search&X-MB=0&X-Search-Action=view'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'alex.costanza98@gmail.com' ,
        'alexandru.serban98@e-uvt.ro',
         msg
    )
    print('HEY EMAIL HAS BEEN SENT')

    server.quit()

while(True):
    check_price()
    time.sleep(60 * 60)
