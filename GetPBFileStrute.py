#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
from ProtoType import ProtoType
from ProtoPorperty import ProtoPorperty

class PBFile(object):
    def __init__(self):
        self.classList = None
        self.baseClassList = [ProtoType('int32'),ProtoType('string'),ProtoType('int64'),ProtoType('uint64'),ProtoType('uint32')]

    def getProtoAllTypeString(self,fileContentString,typeName):
        reString = '('+typeName+r'\s\w+\s*\{.*?\})'
        data = re.compile(reString,re.S)
        result = data.findall(fileContentString)
        return result

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
    def getPropertyListWithCode(self,propertyString,classList):
        '''
        return [ProtoPorperty]
        '''
        propertyList = []
        propertyCodeList = propertyString.splitlines()
        propertyCodeList = propertyCodeList[1:-1]
        for codeString in propertyCodeList:
            codeList = codeString.split()
            if len(codeList) == 0:
                continue
            if codeList[0] != 'message':
                if codeList[0] == 'repeated':
                    codeList = codeList[1:]
                findClass = False
                for classType in classList:
                    if codeList[0] == classType.typeName:
                        protoPorpertyObj = ProtoPorperty(codeList[1],classType)
                        if codeList[0] == 'repeated':
                            protoPorpertyObj.isRepeat = True
                        propertyList.append(protoPorpertyObj)
                        findClass = True
                        break
                if findClass == False:
                    protoPorpertyObj = ProtoPorperty(codeList[1],ProtoType(codeList[0]))
                    if codeList[0] == 'repeated':
                        protoPorpertyObj.isRepeat = True
                    propertyList.append(protoPorpertyObj)
                    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
                    print('找不到类型'+codeList[0]+'已自动生成类型❗❗️❗️❗️❗️\n')
                    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
        return propertyList

    def getProtoTypeList(self,protoFilePath):
        '''
        return ProtoType List
        '''
        protoFile = open(protoFilePath)
        protoFileString = protoFile.read()
        protoFile.close()

        # 找到所有的枚举类型并清除掉
        allEnumString = self.getProtoAllTypeString(protoFileString,'enum')
        for enumString in allEnumString:
            protoFileString = protoFileString.replace(enumString,'')

        # 找到所有的message类型
        allMessageString = self.getProtoAllTypeString(protoFileString,'message')
        typeList = []
        classCodeDic = {}
        for codeString in allMessageString:
            aType = ProtoType(self.getClassNameWithCode(codeString))
            typeList.append(aType)
            classCodeDic[aType.typeName] = codeString
        self.classList = typeList
        for pbClass in self.classList:
            className = pbClass.typeName
            pbClass.propertyList = self.getPropertyListWithCode(classCodeDic[className],typeList+self.baseClassList)
        

obj = PBFile()
obj.getProtoTypeList('/Users/liuyudi/PKGame/Foreign/proto-hago-ktv-api-biz/ktvapibiz.proto')
