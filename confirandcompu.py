import copy

import computing
import Fileparsing

totaladd=72
totalmul=391

MUL8LIP=['mul8u_EXZ','mul8u_150Q','mul8u_CK5']
MUL8LIP_area=[11,31,46]
ADD16LIP=['add16u_0EM','add16u_08F','add16u_1JH']
ADD16LIP_area=[15,20,21]


def confirgure(_list,peizhi,N): # Forming an approximate configuration according to peishi
    sum=0
    for i in range(0, N):
        obj = _list[i]
        if obj['functions']['function'] == 'add':
            if int(peizhi[i])>0:
              obj['functions']['function']= ADD16LIP[peizhi[i]-1]
              sum=sum+ADD16LIP_area[peizhi[i]-1]
        if obj['functions']['function'] == 'mul':
            if int(peizhi[i]) > 0:
                obj['functions']['function']= MUL8LIP[peizhi[i]-1]
                sum = sum + MUL8LIP_area[peizhi[i] - 1]
    return _list,sum
def singleapproximate(_list,_list3,N,MED1): #The error of a single approximation unit is used when Peishi is all zero
    ADD16LIPcuowu = []
    MUL8LIPcuowu = []
    _list1=copy.deepcopy(_list)
    _list2 = copy.deepcopy(_list)
    sign=0
    sign1 = 0
    for i in range(0, N):
        obj = _list1[i]
        obj1 = _list2[i]
        if sign==0:
            if obj['functions']['function'] == 'add':
                for j in range(0,len(ADD16LIP)):
                  obj['functions']['function']=ADD16LIP[j]
                  MED = computing.GAerror1(_list1)
                  if MED<=MED1:
                    ADD16LIPcuowu.append(MED)
                sign=1
        if sign1==0:
            if obj1['functions']['function'] == 'mul':
                for j in range(0,len(MUL8LIP)):
                  obj1['functions']['function']=MUL8LIP[j]
                  MED = computing.GAerror1(_list2)
                  if MED<=MED1:
                    MUL8LIPcuowu.append(MED)
                sign1=1
    return ADD16LIPcuowu,MUL8LIPcuowu









