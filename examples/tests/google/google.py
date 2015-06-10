# -*- coding: utf-8 -*-

import nightwatch_utils
import commands as browser
from nightwatch_utils import driver_path

#Start your test here...

def googletest():
    this = nightwatch_utils.driver(driver_path) #This should always be present

    #start your commands here
    browser.getURL(this, 'http://www.google.com')
    browser.clickClearAndType(this, '#lst-ib', 'automated testing')
    browser.clickRetry(this,'.lsb[value="Search"]')
    browser.pause(5) # pause for 5 seconds
    browser.snapshot(this,'google-results.png')
    browser.quit(this)

googletest()
