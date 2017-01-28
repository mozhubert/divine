#!/usr/bin/python
#coding:utf-8

import random
import toss

class Toss:
    def __init__(self):
        self.rightblock = True
        self.leftblock = True

    def toss(self):
        leftodds = random.random()
        rightodds = random.random()

        if leftodds > 0.5:
            self.leftblock = True
        else:
            self.leftblock = False

        if rightodds > 0.5:
            self.rightblock = True
        else:
            self.rightblock = False

    def throw(self):
        blocks = toss.Toss()
        times = 0
        while True:
            raw_input("請按Enter擲筊")
            blocks.toss()

            if (blocks.leftblock == True and blocks.rightblock == True):
                print "笑筊"
                return False
                # break
            elif (blocks.leftblock == False and blocks.rightblock == False):
                print "蓋筊"
                return False
                # break
            else:
                times = times + 1
                print "允筊"
                if times == 3:
                    return True


