import sqsp_utils
import module1 as sqsp
import time

def test(): # Similar to JavaScript, I'm creating a function that executes the code below.

    #specify the site url, email and password
    sqsp_utils.login()

    sqsp.goToPages()
    sqsp.checkPageForBlock()
    sqsp.end()

test()
