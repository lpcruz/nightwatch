# -*- coding: utf-8 -*-

import nightwatch_utils
from nightwatch_utils import time, start_time
import os
import sys


def clickRetry (driver, css_selector):
    try:
        driver.find_element_by_css_selector(css_selector).click()
        time.sleep(1) #pause 1 second
        driver.find_element_by_css_selector(css_selector).click()
        print "✔    Clicked on <" + css_selector + ">"
    except:

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
        driver.save_screenshot('screens/')

    return (driver, css_selector, content)


def snapshot(driver, image_name):
    try:
        driver.save_screenshot('screens/' + image_name);
        print "✔    Took screenshot after " + ("%s seconds" % (time.time() - start_time))
    except:
        print "X    Unable to take a screenshot"

    return (driver, image_name)


def getURL(driver, url):
    try:
        driver.get(url)
        print "✔    Element <body> with the url of "+ url + " present after " + ("%s seconds" % (time.time() - start_time))
    except:
        print "X    Unable to load " + url + " after " + ("%s seconds" % (time.time() - start_time))

    return (driver, url)


def pause(seconds):
    time.sleep(seconds)

    print "✔    Paused Browser for " + str(seconds) + " seconds"

    return (time)


def quit (driver):
    try:
        driver.quit()
        print ""
        print "Done, without errors."
        print "Finished test in " + ("%s seconds" % (time.time() - start_time))
    except:
        print "X    Test Failed. See Errors in log."

    return driver
