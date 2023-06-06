# import pandas as pd
import math
from ctypes import *
import numpy as np
from decimal import *
import random

# import xiaxiaxianjisuan
# import DFGparsing

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
ADD174 = 0
ADD174 = cdll.LoadLibrary("./approlib/add16u_08F.so")


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
def firerrorcomputing(obj1):
    # q=excel_one_line_to_list()
    n1=0 #随机变量生成范围
    n2=255 #随机变量生成范围
    xunh=100000 #循环次数也就是随机变量的个数
    sum=[]
    # for i in range (0,len(q[0])-3):
    for j in range(0,xunh):
        a= random.randint(n1, n2)
        b=random.randint(n1, n2)
        d = random.randint(n1, n2)
        c=random.randint(n1, n2)
        a1= random.randint(n1, n2)
        b1=random.randint(n1, n2)
        d1 = random.randint(n1, n2)

        a2= random.randint(n1, n2)
        b2=random.randint(n1, n2)
        d2 = random.randint(n1, n2)
        c2=random.randint(n1, n2)
        a3= random.randint(n1, n2)
        b3=random.randint(n1, n2)

        input1=a
        input2=21
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


        input1=b
        input2=20
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


        input1=c
        input2=17
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


        input1=d
        input2=25
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


        input1=a1
        input2=30
        if obj1[4]['functions']['function'] == 'mul':
            obj1[4]['functions']['write_data'] = input1 * input2
        if obj1[4]['functions']['function'] == 'mul8u_Y48':
            obj1[4]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[4]['functions']['function'] == 'mul8u_150Q':
            obj1[4]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[4]['functions']['function'] == 'mul8u_2P7':
            obj1[4]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[4]['functions']['function'] == 'mul8u_KEM':
            obj1[4]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[4]['functions']['function'] == 'mul8u_CK5':
            obj1[4]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)
        if obj1[4]['functions']['function'] == 'mul8u_EXZ':
            obj1[4]['functions']['write_data'] = MUL10.mul8u_EXZ(input1, input2)


        input1=b1
        input2=0
        if obj1[5]['functions']['function'] == 'mul':
            obj1[5]['functions']['write_data'] = input1 * input2
        if obj1[5]['functions']['function'] == 'mul8u_Y48':
            obj1[5]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[5]['functions']['function'] == 'mul8u_150Q':
            obj1[5]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[5]['functions']['function'] == 'mul8u_2P7':
            obj1[5]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[5]['functions']['function'] == 'mul8u_KEM':
            obj1[5]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[5]['functions']['function'] == 'mul8u_CK5':
            obj1[5]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)
        if obj1[5]['functions']['function'] == 'mul8u_EXZ':
            obj1[5]['functions']['write_data'] = MUL10.mul8u_EXZ(input1, input2)




        input1=d1
        input2=45
        if obj1[6]['functions']['function'] == 'mul':
            obj1[6]['functions']['write_data'] = input1 * input2
        if obj1[6]['functions']['function'] == 'mul8u_Y48':
            obj1[6]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[6]['functions']['function'] == 'mul8u_150Q':
            obj1[6]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[6]['functions']['function'] == 'mul8u_2P7':
            obj1[6]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[6]['functions']['function'] == 'mul8u_KEM':
            obj1[6]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[6]['functions']['function'] == 'mul8u_CK5':
            obj1[6]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)
        if obj1[6]['functions']['function'] == 'mul8u_EXZ':
            obj1[6]['functions']['write_data'] = MUL10.mul8u_EXZ(input1, input2)


        input1=a2
        input2=45
        if obj1[7]['functions']['function'] == 'mul':
            obj1[7]['functions']['write_data'] = input1 * input2
        if obj1[7]['functions']['function'] == 'mul8u_Y48':
            obj1[7]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[7]['functions']['function'] == 'mul8u_150Q':
            obj1[7]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[7]['functions']['function'] == 'mul8u_2P7':
            obj1[7]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[7]['functions']['function'] == 'mul8u_KEM':
            obj1[7]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[7]['functions']['function'] == 'mul8u_CK5':
            obj1[7]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)
        if obj1[7]['functions']['function'] == 'mul8u_EXZ':
            obj1[7]['functions']['write_data'] = MUL10.mul8u_EXZ(input1, input2)

        input1 = b2
        input2 = 16
        if obj1[8]['functions']['function'] == 'mul':
            obj1[8]['functions']['write_data'] = input1 * input2
        if obj1[8]['functions']['function'] == 'mul8u_Y48':
            obj1[8]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[8]['functions']['function'] == 'mul8u_150Q':
            obj1[8]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[8]['functions']['function'] == 'mul8u_2P7':
            obj1[8]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[8]['functions']['function'] == 'mul8u_KEM':
            obj1[8]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[8]['functions']['function'] == 'mul8u_CK5':
            obj1[8]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)
        if obj1[8]['functions']['function'] == 'mul8u_EXZ':
            obj1[8]['functions']['write_data'] = MUL10.mul8u_EXZ(input1, input2)

        input1 = c2
        input2 = 15
        if obj1[9]['functions']['function'] == 'mul':
            obj1[9]['functions']['write_data'] = input1 * input2
        if obj1[9]['functions']['function'] == 'mul8u_Y48':
            obj1[9]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[9]['functions']['function'] == 'mul8u_150Q':
            obj1[9]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[9]['functions']['function'] == 'mul8u_2P7':
            obj1[9]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[9]['functions']['function'] == 'mul8u_KEM':
            obj1[9]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[9]['functions']['function'] == 'mul8u_CK5':
            obj1[9]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)
        if obj1[9]['functions']['function'] == 'mul8u_EXZ':
            obj1[9]['functions']['write_data'] = MUL10.mul8u_EXZ(input1, input2)

        input1 = d2
        input2 = 23
        if obj1[10]['functions']['function'] == 'mul':
            obj1[10]['functions']['write_data'] = input1 * input2
        if obj1[10]['functions']['function'] == 'mul8u_Y48':
            obj1[10]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[10]['functions']['function'] == 'mul8u_150Q':
            obj1[10]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[10]['functions']['function'] == 'mul8u_2P7':
            obj1[10]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[10]['functions']['function'] == 'mul8u_KEM':
            obj1[10]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[10]['functions']['function'] == 'mul8u_CK5':
            obj1[10]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)
        if obj1[10]['functions']['function'] == 'mul8u_EXZ':
            obj1[10]['functions']['write_data'] = MUL10.mul8u_EXZ(input1, input2)

        input1 = a3
        input2 = 22
        if obj1[11]['functions']['function'] == 'mul':
            obj1[11]['functions']['write_data'] = input1 * input2
        if obj1[11]['functions']['function'] == 'mul8u_Y48':
            obj1[11]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[11]['functions']['function'] == 'mul8u_150Q':
            obj1[11]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[11]['functions']['function'] == 'mul8u_2P7':
            obj1[11]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[11]['functions']['function'] == 'mul8u_KEM':
            obj1[11]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[11]['functions']['function'] == 'mul8u_CK5':
            obj1[11]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)
        if obj1[11]['functions']['function'] == 'mul8u_EXZ':
            obj1[11]['functions']['write_data'] = MUL10.mul8u_EXZ(input1, input2)

        input1 = b3
        input2 = 20
        if obj1[12]['functions']['function'] == 'mul':
            obj1[12]['functions']['write_data'] = input1 * input2
        if obj1[12]['functions']['function'] == 'mul8u_Y48':
            obj1[12]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[12]['functions']['function'] == 'mul8u_150Q':
            obj1[12]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[12]['functions']['function'] == 'mul8u_2P7':
            obj1[12]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[12]['functions']['function'] == 'mul8u_KEM':
            obj1[12]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[12]['functions']['function'] == 'mul8u_CK5':
            obj1[12]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)
        if obj1[12]['functions']['function'] == 'mul8u_EXZ':
            obj1[12]['functions']['write_data'] = MUL10.mul8u_EXZ(input1, input2)


        input1=obj1[0]['functions']['write_data']
        input2=obj1[1]['functions']['write_data']
        # print(input1, input2)
        # print(a, obj1[0]['functions']['function'])
        if obj1[13]['functions']['function'] == 'add':
            obj1[13]['functions']['write_data'] = input1 + input2
        if obj1[13]['functions']['function'] == 'add16u_0RN':
            obj1[13]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[13]['functions']['function'] == 'add16u_0EM':
            obj1[13]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[13]['functions']['function'] == 'add16u_1JH':
            obj1[13]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[13]['functions']['function'] == 'add16u_073':
            obj1[13]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[13]['functions']['function'] == 'add16u_0M0':
            obj1[13]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)
        if obj1[13]['functions']['function'] == 'add16u_08F':
            obj1[13]['functions']['write_data'] = ADD174.add16u_08F(input1, input2)


        input1=obj1[13]['functions']['write_data']
        input2=obj1[2]['functions']['write_data']
        # print(input1, input2)
        if obj1[14]['functions']['function'] == 'add':
            obj1[14]['functions']['write_data'] = input1 + input2
        if obj1[14]['functions']['function'] == 'add16u_0RN':
            obj1[14]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[14]['functions']['function'] == 'add16u_0EM':
            obj1[14]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[14]['functions']['function'] == 'add16u_1JH':
            obj1[14]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[14]['functions']['function'] == 'add16u_073':
            obj1[14]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[14]['functions']['function'] == 'add16u_0M0':
            obj1[14]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)
        if obj1[14]['functions']['function'] == 'add16u_08F':
            obj1[14]['functions']['write_data'] = ADD174.add16u_08F(input1, input2)

        input1=obj1[14]['functions']['write_data']
        input2=obj1[3]['functions']['write_data']
        # print(input1, input2)
        if obj1[15]['functions']['function'] == 'add':
            obj1[15]['functions']['write_data'] = input1 + input2
        if obj1[15]['functions']['function'] == 'add16u_0RN':
            obj1[15]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[15]['functions']['function'] == 'add16u_0EM':
            obj1[15]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[15]['functions']['function'] == 'add16u_1JH':
            obj1[15]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[15]['functions']['function'] == 'add16u_073':
            obj1[15]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[15]['functions']['function'] == 'add16u_0M0':
            obj1[15]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)
        if obj1[15]['functions']['function'] == 'add16u_08F':
            obj1[15]['functions']['write_data'] = ADD174.add16u_08F(input1, input2)


        input1=obj1[15]['functions']['write_data']
        input2=obj1[4]['functions']['write_data']
        # print(input1, input2)
        if obj1[16]['functions']['function'] == 'add':
            obj1[16]['functions']['write_data'] = input1 + input2
        if obj1[16]['functions']['function'] == 'add16u_0RN':
            obj1[16]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[16]['functions']['function'] == 'add16u_0EM':
            obj1[16]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[16]['functions']['function'] == 'add16u_1JH':
            obj1[16]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[16]['functions']['function'] == 'add16u_073':
            obj1[16]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[16]['functions']['function'] == 'add16u_0M0':
            obj1[16]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)
        if obj1[16]['functions']['function'] == 'add16u_08F':
            obj1[16]['functions']['write_data'] = ADD174.add16u_08F(input1, input2)


        input1=obj1[16]['functions']['write_data']
        input2=obj1[5]['functions']['write_data']
        # print(input1, input2)
        if obj1[17]['functions']['function'] == 'add':
            obj1[17]['functions']['write_data'] = input1 + input2
        if obj1[17]['functions']['function'] == 'add16u_0RN':
            obj1[17]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[17]['functions']['function'] == 'add16u_0EM':
            obj1[17]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[17]['functions']['function'] == 'add16u_1JH':
            obj1[17]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[17]['functions']['function'] == 'add16u_073':
            obj1[17]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[17]['functions']['function'] == 'add16u_0M0':
            obj1[17]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)
        if obj1[17]['functions']['function'] == 'add16u_08F':
            obj1[17]['functions']['write_data'] = ADD174.add16u_08F(input1, input2)


        input1=obj1[17]['functions']['write_data']
        input2=obj1[6]['functions']['write_data']
        # print(input1, input2)
        if obj1[18]['functions']['function'] == 'add':
            obj1[18]['functions']['write_data'] = input1 + input2
        if obj1[18]['functions']['function'] == 'add16u_0RN':
            obj1[18]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[18]['functions']['function'] == 'add16u_0EM':
            obj1[18]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[18]['functions']['function'] == 'add16u_1JH':
            obj1[18]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[18]['functions']['function'] == 'add16u_073':
            obj1[18]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[18]['functions']['function'] == 'add16u_0M0':
            obj1[18]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)
        if obj1[18]['functions']['function'] == 'add16u_08F':
            obj1[18]['functions']['write_data'] = ADD174.add16u_08F(input1, input2)

        input1=obj1[18]['functions']['write_data']
        input2=obj1[7]['functions']['write_data']
        # print(input1, input2)
        if obj1[19]['functions']['function'] == 'add':
            obj1[19]['functions']['write_data'] = input1 + input2
        if obj1[19]['functions']['function'] == 'add16u_0RN':
            obj1[19]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[19]['functions']['function'] == 'add16u_0EM':
            obj1[19]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[19]['functions']['function'] == 'add16u_1JH':
            obj1[19]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[19]['functions']['function'] == 'add16u_073':
            obj1[19]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[19]['functions']['function'] == 'add16u_0M0':
            obj1[19]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)
        if obj1[19]['functions']['function'] == 'add16u_08F':
            obj1[19]['functions']['write_data'] = ADD174.add16u_08F(input1, input2)


        input1=obj1[19]['functions']['write_data']
        input2=obj1[8]['functions']['write_data']
        # print(input1, input2)
        if obj1[20]['functions']['function'] == 'add':
            obj1[20]['functions']['write_data'] = input1 + input2
        if obj1[20]['functions']['function'] == 'add16u_0RN':
            obj1[20]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[20]['functions']['function'] == 'add16u_0EM':
            obj1[20]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[20]['functions']['function'] == 'add16u_1JH':
            obj1[20]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[20]['functions']['function'] == 'add16u_073':
            obj1[20]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[20]['functions']['function'] == 'add16u_0M0':
            obj1[20]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)
        if obj1[20]['functions']['function'] == 'add16u_08F':
            obj1[20]['functions']['write_data'] = ADD174.add16u_08F(input1, input2)



        input1=obj1[20]['functions']['write_data']
        input2=obj1[9]['functions']['write_data']
        # print(input1, input2)
        if obj1[21]['functions']['function'] == 'add':
            obj1[21]['functions']['write_data'] = input1 + input2
        if obj1[21]['functions']['function'] == 'add16u_0RN':
            obj1[21]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[21]['functions']['function'] == 'add16u_0EM':
            obj1[21]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[21]['functions']['function'] == 'add16u_1JH':
            obj1[21]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[21]['functions']['function'] == 'add16u_073':
            obj1[21]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[21]['functions']['function'] == 'add16u_0M0':
            obj1[21]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)
        if obj1[21]['functions']['function'] == 'add16u_08F':
            obj1[21]['functions']['write_data'] = ADD174.add16u_08F(input1, input2)


        input1=obj1[21]['functions']['write_data']
        input2=obj1[10]['functions']['write_data']
        # print(input1, input2)
        if obj1[22]['functions']['function'] == 'add':
            obj1[22]['functions']['write_data'] = input1 + input2
        if obj1[22]['functions']['function'] == 'add16u_0RN':
            obj1[22]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[22]['functions']['function'] == 'add16u_0EM':
            obj1[22]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[22]['functions']['function'] == 'add16u_1JH':
            obj1[22]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[22]['functions']['function'] == 'add16u_073':
            obj1[22]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[22]['functions']['function'] == 'add16u_0M0':
            obj1[22]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)
        if obj1[22]['functions']['function'] == 'add16u_08F':
            obj1[22]['functions']['write_data'] = ADD174.add16u_08F(input1, input2)


        input1=obj1[22]['functions']['write_data']
        input2=obj1[11]['functions']['write_data']
        # print(input1, input2)
        if obj1[23]['functions']['function'] == 'add':
            obj1[23]['functions']['write_data'] = input1 + input2
        if obj1[23]['functions']['function'] == 'add16u_0RN':
            obj1[23]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[23]['functions']['function'] == 'add16u_0EM':
            obj1[23]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[23]['functions']['function'] == 'add16u_1JH':
            obj1[23]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[23]['functions']['function'] == 'add16u_073':
            obj1[23]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[23]['functions']['function'] == 'add16u_0M0':
            obj1[23]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)
        if obj1[23]['functions']['function'] == 'add16u_08F':
            obj1[23]['functions']['write_data'] = ADD174.add16u_08F(input1, input2)


        input1=obj1[23]['functions']['write_data']
        input2=obj1[12]['functions']['write_data']
        # print(input1, input2)
        if obj1[24]['functions']['function'] == 'add':
            obj1[24]['functions']['write_data'] = input1 + input2
        if obj1[24]['functions']['function'] == 'add16u_0RN':
            obj1[24]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[24]['functions']['function'] == 'add16u_0EM':
            obj1[24]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[24]['functions']['function'] == 'add16u_1JH':
            obj1[24]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[24]['functions']['function'] == 'add16u_073':
            obj1[24]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[24]['functions']['function'] == 'add16u_0M0':
            obj1[24]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)
        if obj1[24]['functions']['function'] == 'add16u_08F':
            obj1[24]['functions']['write_data'] = ADD174.add16u_08F(input1, input2)


        ed1=abs((a * 21 + b * 20 + c * 17 + d * 25 + a1 * 30 + b1 * 0 + d1 * 45 + a2 * 45 + b2 * 16 + c2 * 15 + d2 * 23 + a3 * 22 + b3 * 20)-obj1[24]['functions']['write_data'])
        sum.append(ed1)
    summ=0
    q=0
    for i in range(0,len(sum)):
        summ=summ+sum[i]
    Med = summ / len(sum)
    # PSNR=10*math.log10(255*255/Med)
    # q=(PSNR/34)*100
    # return q
    return Med
# if __name__ == '__main__':
#     _list = DFGparsing.reg.search_order()
#     for i in range(0,len(_list)):
#         obj = _list[i]
#         if obj['functions']['function'] == 'add':
#             obj['functions']['function']='add16u_1JH'
#         if obj['functions']['function'] == 'mul':
#             obj['functions']['function']='mul8u_KEM'
#     obj1=_list
#     psnr=firerrorcomputing(obj1)
#     print(psnr)
#

