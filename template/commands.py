# -*- coding: utf-8 -*-

import nightwatch_utils
from nightwatch_utils import time, start_time
import os
import sys
from termcolor import colored
success = colored("✔   ","green")
fail = colored("X   ","red")

def setBrowserSize(driver,length,width):
    driver.set_window_size(length,width)

    return (driver, length, width)

def click(driver,css_selector):
    driver.find_element_by_css_selector(css_selector).click()
    return driver, css_selector

def waitForElementPresent(driver, css_selector,seconds):
    try:
        driver.find_element_by_css_selector(css_selector)
        driver.implicitly_wait(seconds)
        print success + "Element " + "<" + css_selector + ">" + " present after " + ("%s seconds" % (time.time() - start_time))

    except:
        print fail + "Unable to locate " + css_selector
        driver.save_screenshot('screens/fails/unable-to-locate-' +  css_selector + '-in-DOM.png')
        print fail + "Sent a screenshot to the fails folder in screen/fails"
        driver.quit()

def clickRetry (driver, css_selector):
    try:
        driver.find_element_by_css_selector(css_selector).click()
        time.sleep(1) #pause 1 second
        driver.implicitly_wait(20)
        print success + "Clicked on <" + css_selector + ">" + " at " + ("%s seconds" % (time.time() - start_time))
    except:

        driver.find_element_by_css_selector(css_selector).click()
        print fail + "Unable to locate " + css_selector + " and took screenshot of failure"
        driver.save_screenshot('screens/fails/unable-to-click-' + css_selector + '.png')
        driver.quit()

    return (driver, css_selector)

def clickAndType(driver,css_selector,content):
    try:
        driver.implicitly_wait(20)
        driver.find_element_by_css_selector(css_selector).click()
        driver.find_element_by_css_selector(css_selector).send_keys(content)
    except:
        print fail + "Unable to locate <" + css_selector + ">" + "and unable to type " + " '" + content + "' "
        driver.save_screenshot('screens/fails/unable-to-clickAndType-' + css_selector + '-.png')
        driver.quit()

    return (driver, css_selector, content)

def clickClearAndType (driver, css_selector, content):
    try:
        driver.implicitly_wait(20)
        driver.find_element_by_css_selector(css_selector).click()
        driver.find_element_by_css_selector(css_selector).clear()
        driver.find_element_by_css_selector(css_selector).send_keys(content)
        print success + "Clicked on <" + css_selector + ">" + " and typed" + " '" + content + "' "
    except:
        print fail + "Unable to locate <" + css_selector + ">" + "and unable to type " + " '" + content + "' "
        driver.save_screenshot('screens/fails/unable-to-clickClearAndType-' + css_selector + '.png')
        driver.quit()

    return (driver, css_selector, content)


def snapshot(driver, image_name):
    try:
        time.sleep(5)
        driver.implicitly_wait(20)
        driver.save_screenshot('./screens/' + image_name + '.png')
        print success + "Recorded screenshot " + "'" + image_name + '.png' + "'" + " after " + ("%s seconds" % (time.time() - start_time))
    except:
        print fail + "Unable to take a screenshot"

    return (time, driver, image_name)


def getURL(driver, url):
    try:
        driver.get(url)
        print success + "Navigated to  "+ url + " after " + ("%s seconds" % (time.time() - start_time))
    except:
        print fail + "Unable to load " + url + " after " + ("%s seconds" % (time.time() - start_time))
        driver.save_screenshot('screens/fails/unable-to-get-'+ url)
        driver.quit()

    return (driver, url)

def uploadFile(driver,direc,file):
    try:
        driver.find_element_by_css_selector('input[type="file"]').send_keys(os.getcwd() + direc + file)
        print success + "Sent " + str(file) + " to file upload at " + ("%s seconds" % (time.time() - start_time))
    except:
        print fail + "Unable to upload file"
        driver.save_screenshot('screens/fails/unable-to-upload')

def pause(seconds):
    time.sleep(seconds)

    print success + "Paused Browser for " + str(seconds) + " seconds"

    return (time)

def refresh(driver):
    try:
        driver.refresh()
        time.sleep(1)
        print success + "Refreshed Browser at " + ("%s seconds" % (time.time() - start_time))
    except:
        print fail +"Unable to Refresh"

def quit (driver):
    try:
        driver.quit()
        print ""
        print colored("Done, without errors.", "green")
        print "Finished test in " + ("%s seconds" % (time.time() - start_time))

    except:
        print colored("Test Failed. See Errors in log.","red")

    return driver
