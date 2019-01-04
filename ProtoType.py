#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ProtoPorperty import ProtoPorperty
class ProtoType(object):
    def __init__(self,typeName:str,propertyList = None):
        self.typeName = typeName
        self.propertyList = propertyList
basePropertyList = {'int32':ProtoType('int32'),'string':ProtoType('string'),'int64':ProtoType('int64'),'uint64':ProtoType('uint64'),'uint32':ProtoType('uint32')}