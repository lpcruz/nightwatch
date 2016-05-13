# -*- coding: utf-8 -*-

import nightwatch_utils
import commands as browser
from nightwatch_utils import driver_path
from sqsp_utils import this


def goToPages():
    browser.waitForElementPresent(this, '.sqs-damask-menu-item-content[data-label="pages"]', 90)
    browser.clickRetry(this, '.sqs-damask-menu-item-content[data-label="pages"]')
    return this

def getFrame():
    browser.switchFrame(this, 'iframe')
    return this

def checkPageForBlock():
    getFrame()
    browser.waitForElementPresent(this,'.sqs-block-html', 90)
    print "There is a text block here"
    return this

def end():
    browser.quit(this)
    return this
