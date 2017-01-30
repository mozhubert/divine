#!/usr/bin/python
#coding:utf-8

import toss
import poem
import random

blocks = toss.Toss()
stick = poem.Poem()

# times = 0
print "請誠心祈求保生大帝，祈求保生大帝賜杯！"
result = blocks.approve()

if result is True:
    while True:
        raw_input("請按 Enter 抽籤")
        drawn_num=random.randint(0,60)
        print stick.content[str(drawn_num)]

        if blocks.approve() is True:
            raw_input("請按 Enter 詢問是否還有下支籤")
            if blocks.throw() is True:
                continue
            else:
                break
        else:
            continue

stick = poem.Poem()
