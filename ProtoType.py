#!/usr/bin/python
# -*- coding: UTF-8 -*-
class ProtoType(object):
    def __init__(self,typeName:str,propertyList = None):
        self.typeName = typeName
        self.propertyList = propertyList

class EnumType(ProtoType):
    def __init__(self,enumDic):
        self.enumDic = enumDic

class DicType(ProtoType):
    def __init__(self,keyType,valueType):
        self.keyType = keyType
        self.valueType = valueType