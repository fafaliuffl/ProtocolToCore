#!/usr/bin/python
# -*- coding: UTF-8 -*-

class ProtoPorperty(object):
    def __init__(self,objectName:str,objectType,isRepeat = False):
        self.objectName = objectName
        self.objectType = objectType
        self.isRepeat = isRepeat

        