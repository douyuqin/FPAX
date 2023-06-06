import copy

import computing
import confirandcompu


def reducesingle(output,peizhi,_lista,N,tarError):
    output1=copy.deepcopy(output)
    exit=0
    for i in range(len(output1)-1,0,-1):

        if (output1[i]>0)&(peizhi[i]==(output1[i]-1)):
            _listb=copy.deepcopy(_lista)
            output1[i]=output1[i]-1
            (_listdangqian, sum1) = confirandcompu.confirgure(_listb, output1, N)  # 根据配置改变应用
            MED = computing.GAerror1(_listdangqian)  # 计算当前配置的MED
            if MED<=tarError:
                exit = 1
                break
        if exit==1:
            break

    for i in range(len(output1)-1,-1,-1):
        if output1[i]>0:
            depth=i
    return output1,sum1,MED,depth,exit
