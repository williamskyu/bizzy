import http.server
import socketserver
import time
import subprocess
import string
import random
from django.db import models
from splinter import Browser

WAIT_TIME = 1

class discountData:
    def __init__(self, cT, cV, mA):
        self.couponType = cT
        self.couponVal = cV
        self.minimumAmt = mA
       

def main():
    browser = Browser("chrome")
    discData = discountData("D", 10, 15)
    shopifyLogin(browser, discData)
    dCode = createDiscount(browser, discData)
    return dCode


def begin(a, b, c):
    browser = Browser("chrome")
    discData = discountData(a, b, c)
    shopifyLogin(browser, discData)
    dCode = createDiscount(browser, discData)
    return dCode


def shopifyLogin(browser, dd):
    # Variables, addl security needed, like encryption key
    accStore = "billiams-bazaar"
    accName = "williamskyu@gmail.com"
    accPass = "bizzy123"
    pageLogin = "https://www.shopify.com/login"
    # Dev Note:
    # If web page changes, many of these hard coded elements
    # will have to change too
    browser.visit(pageLogin)
    # Should add validation to check for these elements
    # browser.fill("subdomain", accStore)
    browser.fill("login", accName)
    browser.fill("password", accPass)
    browser.find_by_text("Log in").first.click()
    time.sleep(WAIT_TIME)
    
    # Some login validation, additional auth page
    # If "login" is in the shop name, could have some false positives
    if "login" in browser.url:
        # Return login error
        writeToLog("LOGIN ERROR! EXITING...")
        terminate()
    writeToLog("SUCESSFULLY LOGGED IN AS: " + accName + "!")



def createDiscount(browser, dd):
    browser.find_by_text("Discounts").last.click()
    time.sleep(WAIT_TIME)
    newCode = randGenCode()
    # Generate random code until you get a unique one
    while newCode in browser.html:
        newCode = randGenCode()
    browser.find_by_text("Add discount code").first.click()
    time.sleep(WAIT_TIME)

    # Start filling out discount form
    browser.fill("discount[code]", newCode)
    if dd.couponType == "D":
        browser.find_by_name("discount[discount_type]").first.select("fixed_amount")
    else:
        browser.find_by_name("discount[discount_type]").first.select("percentage")
    browser.fill("discount[value]", str(dd.couponVal))
    if not dd.minimumAmt == 0:
        browser.find_by_name("discount[applies_to_resource]").first.select("minimum_order_amount")
        browser.fill("discount[minimum_order_amount]", str(dd.minimumAmt))
    browser.find_by_text("Save").first.click()
    time.sleep(WAIT_TIME)
    if "with this discount" in browser.html:
        writeToLog("UNEXPECTED ERROR CREATING DISCOUNT! EXITING...")
        terminate(browser)
    writeToLog("DISCOUNT CREATED SUCCESSFULLY WITH CODE " + newCode + "!")
    time.sleep(WAIT_TIME)
    terminate(browser)
    return newCode

    
def randGenCode():
    c1 = random.choice(string.ascii_letters)
    c2 = random.choice(string.ascii_letters)
    c3 = random.choice(string.ascii_letters)
    c4 = random.choice(string.ascii_letters)
    n1 = random.randint(0,9999)
    return (c1 + c2 + c3 + c4 + str(n1))

    
def terminate(browser):
    browser.quit()
    #exit()


# Function should write to log in full version instead of console print
def writeToLog(s):
    print(s)

    
if __name__ == "__main__":
    main()


    
