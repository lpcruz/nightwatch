# -*- coding: utf-8 -*-

import nightwatch_utils
import commands as browser
from nightwatch_utils import driver_path
from sqsp_utils import this


def end():
    browser.quit(this)
    return this
