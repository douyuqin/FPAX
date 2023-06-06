import copy

import computing
import costperformance
import makepeizhi
import confirandcompu


def produce(depth,peizhi,MUL8LIPcuowu1,ADD16LIPcuowu1,mubiaocuowu,n,_listdangqian,MED,_list,N):
#Used to determine the changed nodes and the increased approximate level

    (xingjiabi, xingjiabiyuanlai, xingjiabihoulai, xingjiabijilu, xingjiabizengjia,
     xingjiabiyuanlaiweizhi,depth) = costperformance.costper(depth,
                                                       _listdangqian,
                                                       peizhi,
                                                       MUL8LIPcuowu1,
                                                       MED,
                                                       ADD16LIPcuowu1,
                                                       mubiaocuowu)

    # Used to solve the problem of depth depletion
    flag=1
    if len(xingjiabizengjia)==0:
        flag=0
        _listdangqian1 = copy.deepcopy(_listdangqian)
        for i in range(0,len(peizhi)):
            obj=_listdangqian[i]
            if peizhi[i]==0:
                xingjiabiyuanlai.append(obj['functions']['function'])
                xingjiabizengjia.append(1)
                depth=i
                break
    if (flag==0)&(len(xingjiabiyuanlai)==0):
        _listdangqian1 = copy.deepcopy(_listdangqian)
        for i in range(0,len(peizhi)):
            obj=_listdangqian[i]
            if peizhi[i]==1:
                xingjiabiyuanlai.append(obj['functions']['function'])
                xingjiabizengjia.append(2)
                depth=i
                break
    #Change approximate configuration based on predicted values and cost performance
    (peizhireducezuizhong, depthrecord) = makepeizhi.make(depth, n, _listdangqian, xingjiabizengjia, xingjiabiyuanlai, xingjiabihoulai, peizhi)
    xingjibi=0
    depth=[]
    for i in range(0, len(peizhireducezuizhong)):
        _lista = copy.deepcopy(_list)
        (_listdangqian, sum1) = confirandcompu.confirgure(_lista, peizhireducezuizhong[i], N)  # 根据配置改变应用
        MED = computing.GAerror1(_listdangqian)  # 计算当前配置的MED
        if MED==0:
            MED=0.000001
        xingjibi1 = sum1 / MED
        if xingjibi1>xingjibi:
            xingjibi=xingjibi1
            output=peizhireducezuizhong[i]
            outputarea=sum1
            error=MED
            depth=depthrecord[i]
    tuichu = 0
    return output,outputarea,error,depth,tuichu



