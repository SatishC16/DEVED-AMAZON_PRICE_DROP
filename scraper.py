import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Quick-Heal-Total-Security-Version/dp/B073VMC9S1/ref=sr_1_3?crid=1IGGRGTQFHJYL&dchild=1&keywords=quick%2Bheal%2Btotal%2Bsecurity&qid=1627915784&sprefix=quic%2Caps%2C776&sr=8-3&th=1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62',
}


def check_price():
	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, 'html.parser')

	# print(soup.prettify())

	title = soup.find(id="productTitle").get_text()
	price = soup.find(id="priceblock_ourprice").get_text()
	c_price = float(price[1:2]+price[3:6])

	print(title.strip())
	print(c_price)

	if(c_price <= 1199):
		send_mail()

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('satishchandan7861@gmail.com', 'wqpksjocjpngdygb')

	subject = 'Price Drop'
	body = 'Check out Amazon \nPrice Drop \nhttps://www.amazon.in/Quick-Heal-Total-Security-Version/dp/B073VMC9S1/ref=sr_1_3?crid=1IGGRGTQFHJYL&dchild=1&keywords=quick%2Bheal%2Btotal%2Bsecurity&qid=1627915784&sprefix=quic%2Caps%2C776&sr=8-3&th=1'

	msg = f'Subject: {subject}\n\n{body}'
	print(msg)

	server.sendmail('satishchandan7861@gmail.com', 'satishchandan786@gmail.com', msg)
	print('Hey Email has been sent!!!')

	server.quit()

while(True):
	check_price()
	time.sleep(60*60)