# -*- coding: utf-8 -*-
'''
Name: Yelp Search test
Desc: Visits Yelp's homepage and searches a type of food
Author: Laurence Cruz
'''


import nightwatch_utils
import commands as browser #you can rename the commands module as anything you want. In this case, we're calling it 'browser'
from nightwatch_utils import driver_path

#Start your test here...

def yelptest():
    this = nightwatch_utils.driver(driver_path) #This should always be present

    #start your commands here
    browser.getURL(this, 'http://www.yelp.com')
    browser.assertElementPresent(this,'body')
    browser.assertElementPresent(this,'#find_desc[name=find_desc]')
    browser.clickClearAndType(this, '#find_desc[name=find_desc]', 'sushi')
    browser.clickRetry(this,'#header-search-submit[title=Search]')
    browser.pause(5) # pause for 5 seconds
    browser.snapshot(this,'yelp-results.png')
    browser.quit(this)

yelptest()
