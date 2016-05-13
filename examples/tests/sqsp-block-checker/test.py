import sqsp_utils
import module1 as sqsp
import time

def test():

    #specify the site url, email and password
    sqsp_utils.login()

    sqsp.goToPages()
    sqsp.checkAllPagesForBlocks()
    sqsp.end()

test()
