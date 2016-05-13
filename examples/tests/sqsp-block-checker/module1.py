# -*- coding: utf-8 -*-

import nightwatch_utils
import commands as browser
from nightwatch_utils import driver_path
from sqsp_utils import this


def goToPages():
    browser.waitForElementPresent(this, '.sqs-damask-menu-item-content[data-label="pages"]', 90)
    browser.clickRetry(this, '.sqs-damask-menu-item-content[data-label="pages"]')
    return this

def checkAllPagesForBlocks():
    regular_page_types = browser.findAllElements(this,'.icon-page')

    for i in regular_page_types:
            print "Hello, world"

    return this, regular_page_types

def getFrame():
    browser.switchFrame(this, 'iframe')
    return this

def checkPageForBlock():
    getFrame()
    try:
        browser.waitForElementPresent(this,'.sqs-block-html', 90)
        print "There is a text block here"
    except:
        print "There isn't a text block here"

    return this


def end():
    browser.quit(this)
    return this
