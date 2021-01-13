from selenium import webdriver
from random import randint
from time import sleep

from discord_webhook import DiscordWebhook


#this is for the setup of the website to be configured and scraped
url = 'https://www.bestbuy.com/site/amd-ryzen-9-5900x-4th-gen-12-core-24-threads-unlocked-desktop-processor-without-cooler/6438942.p?skuId=6438942'
browser = webdriver.Chrome()

#webhook for the discord notification system
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/791708222326177793/_WwP0u2Yc8Qxi6LG5ZEFk_qQ89Ocsn9dkXibrOjAnpbq1fr8EuQELJPzcBnyMdBvfPiM',
                                content='<@&794330080553599017> 5900x is available ' +
                                'https://www.bestbuy.com/site/amd-ryzen-9-5900x-4th-gen-12-core-24-threads-unlocked-desktop-processor-without-cooler/6438942.p?skuId=6438942') 






def main():

    while True:
        
        browser.get(url) #load web page
        body = browser.find_element_by_class_name("fulfillment-add-to-cart-button")#locate the button to add to cart using the class name 
        
        if (body.text == "Add to Cart"):#if the button says add to cart notify right away
            response = webhook.execute() #send discord notification
            #sleep(5) #wait to check if it is still in stock
            
        sleep(randint(9,11))#sleep for a random time between 9-11 seconds
        
main()