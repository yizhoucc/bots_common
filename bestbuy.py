from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import bestbuycred as info
from playsound import playsound
import numpy as np
import time

chrome_driver = "chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)

# driver = webdriver.Chrome(chrome_driver)
RTX3070LINK1 = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"
RTX3070LINK2 = "https://www.bestbuy.com/site/gigabyte-geforce-rtx-3070-8g-gddr6-pci-express-4-0-graphics-card-black/6437912.p?skuId=6437912"
XBOXONETEST = "https://www.bestbuy.com/site/microsoft-xbox-series-s-512-gb-all-digital-console-disc-free-gaming-white/6430277.p?skuId=6430277"
RTX3080="https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"

driver.get(RTX3080)
isComplete = False

def if_day():
    return (time.localtime().tm_hour>8 or time.localtime().tm_hour<19)

# input("manual sign in, Press Enter to continue...")

while not isComplete:
    # find add to cart button
    if if_day():
        try:
            atcBtn = WebDriverWait(driver, np.random.randint(11,20)).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
            )
        except:
            driver.refresh()
            continue

        print("Add to cart button found")

        try:
            # add to cart
            atcBtn.click()
            # go to cart and begin checkout as guest
            driver.get("https://www.bestbuy.com/cart")
            fullxpath="/html/body/div[1]/main/div/div[2]/div[1]/div/div[2]/div[1]/section[2]/div/div/div[4]/div/div[1]/button"
            checkoutBtn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, fullxpath))
            )
            checkoutBtn.click()
            print("Successfully added to cart")
            playsound('ready.mp3')
            isComplete=True
        except:
            driver.get(RTX3080)
            print("Error")
            playsound('ready.mp3')
            continue
    else:
        time.sleep(60)



#         # # fill in email and password
#         # emailField = WebDriverWait(driver, 10).until(
#         #     EC.presence_of_element_located((By.ID, "fld-e"))
#         # )
#         # emailField.send_keys(info.email)

#         # pwField = WebDriverWait(driver, 10).until(
#         #     EC.presence_of_element_located((By.ID, "fld-p1"))
#         # )
#         # pwField.send_keys(info.password)

#         # # click sign in button
#         # signInBtn = WebDriverWait(driver, 10).until(
#         #     EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[3]/button"))
#         # )
#         # signInBtn.click()
#         # print("Signing in")

#         # cont to pay button
#         cont2payxpath="/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button"
#         cont2paybtn = WebDriverWait(driver, 2).until(
#             EC.presence_of_element_located((By.XPATH, cont2payxpath))
#         )
#         cont2paybtn.click()
#         # fill in card cvv
#         cvvField = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.ID, "credit-card-cvv"))
#         )
#         cvvField.send_keys(info.cvv)
#         print("Attempting to place order")

#         # place order
#         placeOrderBtn = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, ".button__fast-track"))
#         )
#         placeOrderBtn.click()

#         isComplete = True
#     except:
#         # make sure this link is the same as the link passed to driver.get() before looping
#         driver.get(RTX3070LINK1)
#         print("Error - restarting bot")
#         continue

# print("Order successfully placed")


