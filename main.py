#!/usr/bin/python
#coding:utf-8

import toss
import poem
import random


agree_list = []
drawn_list = []
blocks = toss.Toss()
stick = poem.Poem()

print "請誠心祈求保生大帝，祈求保生大帝賜杯！"
result = blocks.approve()

if result is True:
    while True:
        raw_input("請按 Enter 抽籤")
        drawn_num=random.randint(0,60)

        if drawn_num in drawn_list:
            drawn_num=random.randint(0,60)
        drawn_list.append(drawn_num)

        if drawn_num is 0:
            print "[  籤王  ]",
            print stick.content[str(drawn_num)]
        else:
            print '[第 {} 首] '.format(drawn_num),
            print stick.content[str(drawn_num)]

        if blocks.approve() is True:
            agree_list.append(drawn_num)
            raw_input("請按 Enter 詢問是否還有下支籤")
            if blocks.throw() is True:
                drawn_list = []
                for items in agree_list:
                    drawn_list.append(items)
                continue
            else:
                break
        else:
            continue

if len(agree_list) > 0:
    print "*** 保生大帝所賜籤詩為 ***"
    for item in agree_list:
        print '[第 {} 首] {}'.format(item, stick.content[str(item)])
