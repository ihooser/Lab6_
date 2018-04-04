'''
Created on Apr 3, 2018

@author: ihooser
'''
import re
import time
from time import gmtime, strftime


from audioop import add
if __name__ == '__main__':
    pass

time_ = time.asctime(time.localtime(time.time()) )

print time_
