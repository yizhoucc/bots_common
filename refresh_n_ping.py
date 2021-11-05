import bs4
from selenium import webdriver
import sys
import time
import os

def refresh(cart_url):

   # prepare the driver
   headers = {
       'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
   }

   driver = webdriver.Chrome()
   driver.get(cart_url)           
   html = driver.page_source
   soup = bs4.BeautifulSoup(html)

   time.sleep(30)

   # now having the page
   noslot = True
   while noslot:
      driver.refresh()
      print("refreshed at time {}".format(time.strftime("%H:%M", time.gmtime())))
      # parse
      html = driver.page_source
      soup = bs4.BeautifulSoup(html)
      time.sleep(60)
      # search for pattern
      slot_pattern = 'Next available'

      try: # try to find the open slot
         next_slot_text = soup.find('h4', class_ ='ufss-slotgroup-heading-text a-text-normal').text
         if slot_pattern in next_slot_text:
            print("\n\n\n SLOTS OPEN! \n\n\n\n")
            os.system('PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'Delivery available\');"')
            noslot = False
            time.sleep(300) # allow some time to click checkout

      except AttributeError:
         continue

      try: # try to find no slot message. if cant, then we have slot
         no_slot_pattern = 'No delivery windows available. New windows are released throughout the day.'
         if no_slot_pattern == soup.find('h4', class_ ='a-alert-heading').text:
            print("NO SLOTS!")

      except AttributeError: 
         try: # try to find the open slot
            next_slot_text = soup.find('h4', class_ ='ufss-slotgroup-heading-text a-text-normal').text
            if slot_pattern in next_slot_text:
               print("\n\n\n SLOTS OPEN! \n\n\n\n")
               os.system('PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'Delivery available\');"')
               noslot = False
               time.sleep(300) # allow some time to click checkout
            else:
               print('debug')
               os.system('PowerShell -Command "Add-Type -AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'Need Debug\');"')
               noslot = True
               time.sleep(60)
         except AttributeError:
            continue

refresh('https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1')