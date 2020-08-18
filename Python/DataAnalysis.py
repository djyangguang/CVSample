#!/usr/bin/python 
#-*- coding:utf-8 -*-
#
file = './data/neutral.txt'

#杩欎簺鏄凡鐭ョ殑鍒嗙被
names = ['drawings', 'hentai', 'neutral', 'porn', 'sexy']
itemList = []

with open(file) as f:
    item = {}

    for line in f.readlines():
        line = line.strip('\n')
        #姣忎釜浠�.jpg'缁撳熬鐨勮锛屼綔涓轰竴涓猧tem鐨勫紑濮�        if line.endswith('.jpg'):
            if item != {}:
                t = item.copy()
                itemList.append(t)
                item.clear()
            item['pic'] = line
        else:
            splits = line.split(' ')
            if len(splits) > 1:
                key = splits[0].strip()
                value = splits[3].strip(')')
                item[key] = value
    #灏嗘渶鍚庝竴item鏀惧叆闃熷垪
    if item != {}:
        itemList.append(item)

maxList = []
itemNumber = len(itemList)
for i in itemList:
    pic = i.get('pic')
    maxKey = max(i, key=i.get)
    # if(maxKey == 'porn'):
    #     print(pic + " : " + str(maxKey))
    maxList.append(maxKey)

for n in names:
    print('%8s : %d' % (n, maxList.count(n)))
    #print(n + ' : ' + str(maxList.count(n)))