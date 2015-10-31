# coding=utf-8
# Created by bl 2015/10/30.

import os
import shutil

basePath = os.getcwd()
pathList = list()

# 获取目录
for dirName in os.listdir(basePath):
    path = os.path.join(basePath, dirName)
    if os.path.isdir(path):
        pathList.append(path)

# print pathList

for path in pathList:
    shutil.copy(basePath+"\ignore.myignore",path+"\ignore.myignore")
    os.chdir(path)
    os.system('svn propdel svn:global-ignores')
    os.system('svn propset svn:ignore -F ignore.myignore .') 
    os.remove(path+"\ignore.myignore")

os.system('pause')
