# import pandas as pd
import math
from ctypes import *
import numpy as np
from decimal import *
import random

# import xiaxiaxianjisuan
# import DFGparsing

ADD8LIP=['add8u_5R3','add8u_5SY','add8u_006','add8u_8ES']
ADD8LIP_area=[63.8,28.2,15,8]
MUL8LIP=['mul8u_Y48','mul8u_2P7','mul8u_KEM','mul8u_150Q']
MUL8LIP_area=[390,386,370,360]
ADD16LIP=['add16u_0RN','add16u_0EM','add16u_1JH','add16u_073']
ADD16LIP_area=[60,57,51,43]
# ADD16LIP=['add16u_0EM','add16u_1JH','add16u_073','add16u_0M0']
# ADD16LIP_area=[57,51,43,36]

ADD1 = 0
ADD1 = cdll.LoadLibrary("./approlib/add8u_5R3.so")
ADD2 = 0
ADD2 = cdll.LoadLibrary("./approlib/add8u_5SY.so")
ADD3 = 0
ADD3 = cdll.LoadLibrary("./approlib/add8u_006.so")
ADD4 = 0
ADD4 = cdll.LoadLibrary("./approlib/add8u_8ES.so")
MUL1 = 0
MUL1 = cdll.LoadLibrary("./approlib/mul8u_Y48.so")
MUL2 = 0
MUL2 = cdll.LoadLibrary("./approlib/mul8u_150Q.so")
MUL3 = 0
MUL3 = cdll.LoadLibrary("./approlib/mul8u_185Q.so")
MUL4 = 0
MUL4 = cdll.LoadLibrary("./approlib/mul8u_13QR.so")
MUL5 = 0
MUL5 = cdll.LoadLibrary("./approlib/mul8u_2HH.so")
MUL6 = 0
MUL6 = cdll.LoadLibrary("./approlib/mul8u_2P7.so")
MUL7 = 0
MUL7 = cdll.LoadLibrary("./approlib/mul8u_CK5.so")
MUL8 = 0
MUL8 = cdll.LoadLibrary("./approlib/mul8u_KEM.so")
# MUL9 = 0
# MUL9 = cdll.LoadLibrary("./approlib/mul8u_QJD.so")
MUL10 = 0
MUL10 = cdll.LoadLibrary("./approlib/mul8u_EXZ.so")


ADD161 = 0
ADD161 = cdll.LoadLibrary("./approlib/add16u_0EM.so")
ADD162 = 0
ADD162 = cdll.LoadLibrary("./approlib/add16u_073.so")
ADD163 = 0
ADD163 = cdll.LoadLibrary("./approlib/add16u_00G.so")
ADD164 = 0
ADD164 = cdll.LoadLibrary("./approlib/add16u_02E.so")


ADD165 = 0
ADD165 = cdll.LoadLibrary("./approlib/add16u_0M0.so")
ADD166 = 0
ADD166 = cdll.LoadLibrary("./approlib/add16u_1E2.so")
ADD167 = 0
ADD167 = cdll.LoadLibrary("./approlib/add16u_1JH.so")
ADD168 = 0
ADD168 = cdll.LoadLibrary("./approlib/add16u_0RN.so")


ADD169 = 0
ADD169 = cdll.LoadLibrary("./approlib/add16se_1Y7.so")
ADD170 = 0
ADD170 = cdll.LoadLibrary("./approlib/add16se_2JY.so")
ADD171 = 0
ADD171 = cdll.LoadLibrary("./approlib/add16se_20J.so")
ADD172 = 0
ADD172 = cdll.LoadLibrary("./approlib/add16se_26Q.so")
ADD173 = 0
ADD173 = cdll.LoadLibrary("./approlib/add16se_2BY.so")

# def excel_one_line_to_list():
#     b = np.arange(0, 256)
#     df = pd.read_excel("222.xlsx", usecols=b,
#                        names=None)  # 读取项目名称和行业领域两列，并不要列名
#     df_li = df.values.tolist()
#     return df_li
def converrorcomputing(obj1):
    # q=excel_one_line_to_list()
    n1=0 #随机变量生成范围
    n2=150 #随机变量生成范围
    xunh=100000 #循环次数也就是随机变量的个数
    sum=[]
    for j in range(0,xunh):
        a= random.randint(n1, n2)
        b=random.randint(n1, n2)
        d = random.randint(n1, n2)
        c=random.randint(n1, n2)
        a1= random.randint(n1, n2)
        b1 = random.randint(n1, n2)
        c1 = random.randint(n1, n2)
        d1 = random.randint(n1, n2)

        input1=a
        input2=b
        if obj1[0]['functions']['function'] == 'mul':
            obj1[0]['functions']['write_data'] = input1 * input2
        if obj1[0]['functions']['function'] == 'mul8u_Y48':
            obj1[0]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[0]['functions']['function'] == 'mul8u_150Q':
            obj1[0]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[0]['functions']['function'] == 'mul8u_2P7':
            obj1[0]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[0]['functions']['function'] == 'mul8u_KEM':
            obj1[0]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[0]['functions']['function'] == 'mul8u_CK5':
            obj1[0]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)
        if obj1[0]['functions']['function'] == 'mul8u_EXZ':
            obj1[0]['functions']['write_data'] = MUL10.mul8u_EXZ(input1, input2)


        input1=c
        input2=d
        if obj1[1]['functions']['function'] == 'mul':
            obj1[1]['functions']['write_data'] = input1 * input2
        if obj1[1]['functions']['function'] == 'mul8u_Y48':
            obj1[1]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[1]['functions']['function'] == 'mul8u_150Q':
            obj1[1]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[1]['functions']['function'] == 'mul8u_2P7':
            obj1[1]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[1]['functions']['function'] == 'mul8u_KEM':
            obj1[1]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[1]['functions']['function'] == 'mul8u_CK5':
            obj1[1]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)
        if obj1[1]['functions']['function'] == 'mul8u_EXZ':
            obj1[1]['functions']['write_data'] = MUL10.mul8u_EXZ(input1, input2)
        input1=a1
        input2=b1
        if obj1[2]['functions']['function'] == 'mul':
            obj1[2]['functions']['write_data'] = input1 * input2
        if obj1[2]['functions']['function'] == 'mul8u_Y48':
            obj1[2]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[2]['functions']['function'] == 'mul8u_150Q':
            obj1[2]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[2]['functions']['function'] == 'mul8u_2P7':
            obj1[2]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[2]['functions']['function'] == 'mul8u_KEM':
            obj1[2]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[2]['functions']['function'] == 'mul8u_CK5':
            obj1[2]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)
        if obj1[2]['functions']['function'] == 'mul8u_EXZ':
            obj1[2]['functions']['write_data'] = MUL10.mul8u_EXZ(input1, input2)
        input1=c1
        input2=d1
        if obj1[3]['functions']['function'] == 'mul':
            obj1[3]['functions']['write_data'] = input1 * input2
        if obj1[3]['functions']['function'] == 'mul8u_Y48':
            obj1[3]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[3]['functions']['function'] == 'mul8u_150Q':
            obj1[3]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[3]['functions']['function'] == 'mul8u_2P7':
            obj1[3]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[3]['functions']['function'] == 'mul8u_KEM':
            obj1[3]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[3]['functions']['function'] == 'mul8u_CK5':
            obj1[3]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)
        if obj1[3]['functions']['function'] == 'mul8u_EXZ':
            obj1[3]['functions']['write_data'] = MUL10.mul8u_EXZ(input1, input2)

        input1=obj1[0]['functions']['write_data']
        input2=obj1[1]['functions']['write_data']
        # print(input1, input2)
        if obj1[4]['functions']['function'] == 'add':
            obj1[4]['functions']['write_data'] = input1 + input2
        if obj1[4]['functions']['function'] == 'add16u_0RN':
            obj1[4]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[4]['functions']['function'] == 'add16u_0EM':
            obj1[4]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[4]['functions']['function'] == 'add16u_1JH':
            obj1[4]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[4]['functions']['function'] == 'add16u_073':
            obj1[4]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[4]['functions']['function'] == 'add16u_0M0':
            obj1[4]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)

        input1=obj1[2]['functions']['write_data']
        input2=obj1[3]['functions']['write_data']
        # print(input1, input2)
        if obj1[5]['functions']['function'] == 'add':
            obj1[5]['functions']['write_data'] = input1 + input2
        if obj1[5]['functions']['function'] == 'add16u_0RN':
            obj1[5]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[5]['functions']['function'] == 'add16u_0EM':
            obj1[5]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[5]['functions']['function'] == 'add16u_1JH':
            obj1[5]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[5]['functions']['function'] == 'add16u_073':
            obj1[5]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[5]['functions']['function'] == 'add16u_0M0':
            obj1[5]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)


        input1=obj1[4]['functions']['write_data']
        input2=obj1[5]['functions']['write_data']
        # print(input1, input2)
        if obj1[6]['functions']['function'] == 'add':
            obj1[6]['functions']['write_data'] = input1 + input2
        if obj1[6]['functions']['function'] == 'add16u_0RN':
            obj1[6]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[6]['functions']['function'] == 'add16u_0EM':
            obj1[6]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[6]['functions']['function'] == 'add16u_1JH':
            obj1[6]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[6]['functions']['function'] == 'add16u_073':
            obj1[6]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[6]['functions']['function'] == 'add16u_0M0':
            obj1[6]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)


        ed =abs((a*b+c*d+a1*b1+c1*d1)-obj1[6]['functions']['write_data'])
        sum.append(abs(ed))
    summ=0
    for o in range(0,len(sum)):
        summ=summ+abs(sum[o])
    MED=summ/len(sum)
    # error=error/59*100
    return MED

# if __name__ == '__main__':
#     _list = DFGparsing.reg.search_order()
#     for i in range(0,len(_list)):
#         obj = _list[i]
#         if obj['functions']['function'] == 'add':
#             obj['functions']['function']='add16u_073'
#         if obj['functions']['function'] == 'mul':
#             obj['functions']['function']='mul8u_150Q'
#     obj1=_list
#     psnr=converrorcomputing(obj1)
#     print(psnr)
