#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
from ProtoType import ProtoType

class PBFile(object):
    def __init__(self):
        self.classList = None
        self.baseClassList = {'int32':ProtoType('int32'),'string':ProtoType('string'),'int64':ProtoType('int64'),'uint64':ProtoType('uint64'),'uint32':ProtoType('uint32')}

    def getProtoAllMessageString(self,fileContentString):
        data = re.compile(r'(message\s\w+\s*\{((?!message\s).)*\})',re.S)
        result = data.findall(fileContentString)
        codeStringList = []
        for mate in result:
            for string in mate:
                if string != '\n':
                    codeStringList.append(string)
        return codeStringList

    def getClassNameWithCode(self,codeString):
        '''
        return ProtoType
        '''
        searchObject = re.search(r'message\s(\w+)\s*{',codeString)
        group = searchObject.group()
        try:
            group = group.replace('{','')
            stringGroup = group.split()
        except error as TypeError:
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
            print('字符串'+codeString+'解析失败❗️❗️❗️❗️❗️\n')
            print('group = '+ group + '\n')
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
        return stringGroup[1]
    def getPropertyListWithCode(self,propertyString):
        '''
        return [ProtoPorperty]
        '''
        propertyCodeList = propertyString.splitlines()
        for protoCode in propertyCodeList:
            print(protoCode)

    def getProtoTypeList(self,protoFilePath):
        '''
        return ProtoType List
        '''
        protoFile = open(protoFilePath)
        protoFileString = protoFile.read()
        protoFile.close()
        allMessageString = self.getProtoAllMessageString(protoFileString)
        typeList = []
        classCodeDic = {}
        for codeString in allMessageString:
            aType = ProtoType(self.getClassNameWithCode(codeString))
            typeList.append(aType)
            classCodeDic[aType.typeName] = codeString
        self.classList = typeList
        for pbClass in self.classList:
            className = pbClass.typeName
            pbClass.propertyList = self.getPropertyListWithCode(classCodeDic[className])

obj = PBFile()
obj.getProtoTypeList('/Users/liuyudi/PKGame/Foreign/proto-hago-ktv-api-biz/ktvapibiz.proto')
