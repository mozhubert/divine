#!/usr/bin/python
#coding:utf-8

import toss
import poem
import random

blocks = toss.Toss()
can_draw = blocks.throw()
stick = poem.Poem()

if can_draw is True:
    while True:
        raw_input("請按Enter抽籤")
        drawn_num=random.randint(0,61)
        print stick.content[str(drawn_num)]
        drawn_agree=blocks.throw()
        if drawn_agree is True:
            raw_input("請按Enter 詢問是否還有下支籤")
            next_draw=blocks.throw()
            if next_draw is False:
                print "沒有下一支了"
                break
            else:
                print "還有下一支籤詩喔"
        else:
            print "不是這隻籤詩喔",
            print "請再抽隻新的！"
            print "============"