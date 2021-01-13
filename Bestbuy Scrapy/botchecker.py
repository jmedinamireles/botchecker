from selenium import webdriver
from random import randint
from time import sleep

from discord_webhook import DiscordWebhook



url = 'https://www.bestbuy.com/site/amd-ryzen-9-5900x-4th-gen-12-core-24-threads-unlocked-desktop-processor-without-cooler/6438942.p?skuId=6438942'
browser = webdriver.Chrome()

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/791708222326177793/_WwP0u2Yc8Qxi6LG5ZEFk_qQ89Ocsn9dkXibrOjAnpbq1fr8EuQELJPzcBnyMdBvfPiM',
                                content='<@&794330080553599017> 5900x is available ' +
                                'https://www.bestbuy.com/site/amd-ryzen-9-5900x-4th-gen-12-core-24-threads-unlocked-desktop-processor-without-cooler/6438942.p?skuId=6438942') 






def main():

    while True:
        
        browser.get(url)
        body = browser.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[6]/div[1]/div/div/div/button')
        

        if (body.text == "Add to Cart"):
            response = webhook.execute()
            sleep(5)
            
        sleep(randint(10,15))
        
main()