# -*- coding: utf-8 -*-

import nightwatch_utils
import commands as browser
from nightwatch_utils import driver_path

# Input values based on your own environment

siteID = raw_input("Site ID: ")
email = raw_input("Email")
password = raw_input("Password")

this = nightwatch_utils.driver(driver_path) # this is the object for chromedriver or phantomJS

def login():
    try:
        browser.setBrowserSize(this,1400,800)
        browser.waitForElementPresent(this,'body',20)
        browser.getURL(this,"http://www." + siteID + ".squarespace.com" + '/config')
        browser.waitForElementPresent(this,'input[name="email"]',20)
        browser.clickClearAndType(this,'input[name="email"]',email)
        browser.waitForElementPresent(this,'input[name="email"]',20)
        browser.clickClearAndType(this,'input[name="password"]',password)
        browser.clickRetry(this,'.footer .submit')
    except:
        browser.snapshot(this,'unable-to-log-in')

    return this, siteID, email, password
