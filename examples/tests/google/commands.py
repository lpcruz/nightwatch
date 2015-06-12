# -*- coding: utf-8 -*-

import nightwatch_utils
from nightwatch_utils import time, start_time
import os
import sys

def assertElementPresent(driver, css_selector):
    try:
        driver.find_element_by_css_selector(css_selector)
        print "✔    Element " + "<" + css_selector + ">" + " present after " + ("%s seconds" % (time.time() - start_time))

    except:
        print "X    Unable to locate " + css_selector

def clickRetry (driver, css_selector):
    try:
        driver.find_element_by_css_selector(css_selector).click()
        time.sleep(1) #pause 1 second
        print "✔    Clicked on <" + css_selector + ">"
    except:

        driver.find_element_by_css_selector(css_selector).click()
        print "X    Unable to locate " + css_selector + " and took screenshot of failure"
        driver.save_screenshot('screens/clickretry-fail.png')
        driver.quit()

    return (driver, css_selector)



def clickClearAndType (driver, css_selector, content):
    try:
        driver.find_element_by_css_selector(css_selector).click()
        driver.find_element_by_css_selector(css_selector).clear()
        driver.find_element_by_css_selector(css_selector).send_keys(content)
        print "✔    Clicked on <" + css_selector + ">" + " and typed" + " '" + content + "' "
    except:
        print "X    Unable to locate <" + css_selector + ">" + "and unable to type " + " '" + content + "' "
        driver.save_screenshot('screens/clickClearAndType-fail.png')

    return (driver, css_selector, content)


def snapshot(driver, image_name):
    try:
        time.sleep(5)
        driver.save_screenshot('screens/' + image_name);
        print "✔    Recorded screenshot " + "'" + image_name + "'" + " after " + ("%s seconds" % (time.time() - start_time))
    except:
        print "X    Unable to take a screenshot"

    return (time, driver, image_name)


def getURL(driver, url):
    try:
        driver.get(url)
        print "✔    Navigated to  "+ url + " after " + ("%s seconds" % (time.time() - start_time))
    except:
        print "X    Unable to load " + url + " after " + ("%s seconds" % (time.time() - start_time))
        driver.save_screenshot('screens/getURL-fail.png')

    return (driver, url)


def pause(seconds):
    time.sleep(seconds)

    print "✔    Paused Browser for " + str(seconds) + " seconds"

    return (time)

def refresh(driver):
    try:
        driver.refresh()
        time.sleep(1)
        print "✔    Refreshed Browser at " + ("%s seconds" % (time.time() - start_time))
    except:
        print "X    Unable to Refresh"

def quit (driver):
    try:
        driver.quit()
        print ""
        print "Done, without errors."
        print "Finished test in " + ("%s seconds" % (time.time() - start_time))

    except:
        print "X    Test Failed. See Errors in log."

    return driver
