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
        # times = 0
        # while True:
        blocks.toss()
        if (blocks.leftblock == True and blocks.rightblock == True):
            print "笑筊"
            return False
        elif (blocks.leftblock == False and blocks.rightblock == False):
            print "蓋筊"
            return False
                # break
        else:
            print "允筊"
            return True

    def approve(self):
        times = 0
        while True:
            raw_input("請按 Enter 擲杯")
            result = self.throw()
            if result is True:
                times = times + 1
                if times == 3:
                    return True
                    break
            else:
                return False
                break


