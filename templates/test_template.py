# -*- coding: utf-8 -*-
'''
This is a template for creating an automated test.
'''

'''Necessary Modules'''
import nightwatch_utils
import commands as browser
from nightwatch_utils import driver_path


#Start your test here...the first step you can do is to make a function!

def yourtest():
    this = nightwatch_utils.driver(driver_path) #This should always be present

    #start your commands here
    #each command requires specific arguments that need to get passed in. For the most part, you'll need to use 'this' as an argument. Refer to commands.py to see what objects are returned
    browser.getURL(this, 'http://www.yourtestsite.com')
    browser.quit() #Each test should quit the browser.

yourtest()
