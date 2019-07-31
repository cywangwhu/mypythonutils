#!/usr/bin/python3.7
#coding:utf-8

import os
import logging

logging.basicConfig(format='%(asctime)s %(levelname)s  %(message)s',filename='test.log',level=logging.DEBUG)

def dir_walk(dirname):
    for parent, dirnames, filenames in os.walk(dirname, followlinks=True):
        for filename in filenames:
            file_path=os.path.join(parent,filename)
            print("filename: %s" % filename)
            print("the filepath: %s\n" % file_path)


def test():
    dir_walk("/home/wcy/android")


if __name__=="__main__":
    logging.info("The process begins.")
    logging.warning("The process begins.")
    test()