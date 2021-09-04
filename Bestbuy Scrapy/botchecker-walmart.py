from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException 


from random import randint
from time import sleep
from datetime import datetime
from discord_webhook import DiscordWebhook


#this is for the setup of the website to be configured and scraped
url = 'https://www.walmart.com/ip/AMD-Ryzen-9-5900X-12-core-24-thread-Desktop-Processor/647899167'
browser = webdriver.Chrome()

#webhook for the discord notification system
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/791708222326177793/_WwP0u2Yc8Qxi6LG5ZEFk_qQ89Ocsn9dkXibrOjAnpbq1fr8EuQELJPzcBnyMdBvfPiM',
								content="<@&794330080553599017> 5900x is available " +
								"https://www.bestbuy.com/site/amd-ryzen-9-5900x-4th-gen-12"+
								"-core-24-threads-unlocked-desktop-processor-without-cooler/6438942.p?skuId=6438942") 

#webhook for failed discord notification
fail_webhook = DiscordWebhook(url="https://discord.com/api/webhooks/791708222326177793/_WwP0u2Yc8Qxi6LG5ZEFk_qQ89Ocsn9dkXibrOjAnpbq1fr8EuQELJPzcBnyMdBvfPiM",
								content="<@&794330080553599017> Failed to detect button") 


def element(): #this is the function to detect if element is on webpage
	
	while True: #keep trying until it is detected otherwise send a discord notification that it is not detected

		try:
			browser.get(url)
			body = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "button spin-button prod-ProductCTA--primary button--primary")))
			if (body.text == "Add to Cart"):#if the button says add to cart notify right away
				response = webhook.execute() #send discord notification if in stock
			return False #false if element is detected

		except (TimeoutException, StaleElementReferenceException):
			#send failure message
			response = fail_webhook.execute()
			pass
			return True 
			
			  


def main():
	 
	while True:
		
		element()
		sleep(randint(9,11))#sleep for a random time between 9-11 seconds

		

browser.get(url) #load web page
body = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "fulfillment-add-to-cart-button")))


main()