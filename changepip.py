#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 00:20:53 2017

@author: kingmo888
"""

import os,shutil,sys,platform

thissys = platform.system()
flag = r'\\' if thissys == 'Windows' else '/'


# search site-packages folder
sitepath="."
for x in sys.path:
    ix=x.find('site-packages')
    if( ix>=0 and x[ix:]=='site-packages'):
      sitepath=x
      break