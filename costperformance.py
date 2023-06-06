import copy

import computing

MUL8LIP = ['mul8u_EXZ', 'mul8u_150Q', 'mul8u_CK5']
MUL8LIP_area = [11, 31, 46]
ADD16LIP = ['add16u_0EM', 'add16u_08F', 'add16u_1JH']
ADD16LIP_area = [15, 20, 21]


def costper(depth, _listdangqian, peizhi, MUL8LIPcuowu1, MED, ADD16LIPcuowu1, mubiaocuowu):
    xingjiabi = []  #Storage cost performance ratio
    xingjiabijilu = []
    xingjiabiyuanlai = []#Record the calculation type before replacement
    xingjiabihoulai = []#Record the calculation type after replacement
    xingjiabizengjia = []#Record the increased approximate level
    xingjiabiyuanlaiweizhi = []#Record the node to be changed
    cuowu = []#Record the error
    for ss in range(0,2):
        if len(xingjiabiyuanlai) ==0:
            for i in range(depth - 2, len(_listdangqian)):
                _listdangqiancopy = copy.deepcopy(_listdangqian)
                obj = _listdangqiancopy[i]
                if (peizhi[i] == 0) & (obj['functions']['function'] == 'mul'):
                    if int(1 in xingjiabijilu) == 0:
                        for j in range(0, len(MUL8LIPcuowu1)):
                            obj['functions']['function'] = MUL8LIP[j]
                            MEDerror = computing.GAerror1(_listdangqiancopy)
                            bb = MEDerror - MED

                            if MEDerror <= mubiaocuowu:
                                if bb <= 0:
                                    bb = 0.0001
                                xingjiabi.append(MUL8LIP_area[j] / bb)
                                xingjiabiyuanlai.append('mul')
                                xingjiabihoulai.append(MUL8LIP[j])
                                xingjiabijilu.append(1)
                                xingjiabizengjia.append(j + 1)
                                xingjiabiyuanlaiweizhi.append(i)
                                cuowu.append(MEDerror)
                            if MEDerror > mubiaocuowu:
                                xingjiabijilu.append(1)

                if (peizhi[i] == 0) & (obj['functions']['function'] == 'add'):
                    if (len(xingjiabijilu) == 0) or (int(2 in xingjiabijilu) == 0):
                        # print('see', ~(2 in xingjiabijilu))
                        for j in range(0, len(ADD16LIPcuowu1)):
                            obj['functions']['function'] = ADD16LIP[j]
                            MEDerror = computing.GAerror1(_listdangqiancopy)
                            bb = MEDerror - MED
                            if MEDerror <= mubiaocuowu:
                                if bb <= 0:
                                    bb = 0.0001
                                xingjiabi.append(ADD16LIP_area[j] / bb)
                                xingjiabiyuanlai.append('add')
                                xingjiabihoulai.append(ADD16LIP[j])
                                xingjiabijilu.append(2)
                                xingjiabizengjia.append(j + 1)
                                xingjiabiyuanlaiweizhi.append(i)
                                cuowu.append(MEDerror)
                            if MEDerror > mubiaocuowu:
                                xingjiabijilu.append(2)

                if (peizhi[i] == 1) & (obj['functions']['function'] == 'mul8u_EXZ'):
                    if (int(3 in xingjiabijilu) == 0):

                        if len(MUL8LIPcuowu1) > 1:
                            for j in range(1, len(MUL8LIPcuowu1)):
                                obj['functions']['function'] = MUL8LIP[j]
                                MEDerror = computing.GAerror1(_listdangqiancopy)
                                bb = MEDerror - MED
                                if MEDerror <= mubiaocuowu:
                                    if bb <= 0:
                                        bb = 0.0001
                                    xingjiabi.append((MUL8LIP_area[j] - MUL8LIP_area[0]) / bb)
                                    xingjiabiyuanlai.append('mul8u_EXZ')
                                    xingjiabihoulai.append(MUL8LIP[j])
                                    xingjiabijilu.append(3)
                                    xingjiabizengjia.append(j + 1)
                                    xingjiabiyuanlaiweizhi.append(i)
                                    cuowu.append(MEDerror)
                                if MEDerror > mubiaocuowu:
                                    xingjiabijilu.append(3)

                if (peizhi[i] == 1) & (obj['functions']['function'] == 'add16u_0EM'):
                    if (int(4 in xingjiabijilu) == 0):
                        if len(ADD16LIPcuowu1) > 1:
                            for j in range(1, len(ADD16LIPcuowu1)):
                                obj['functions']['function'] = ADD16LIP[j]
                                MEDerror = computing.GAerror1(_listdangqiancopy)
                                bb = MEDerror - MED
                                if MEDerror <= mubiaocuowu:
                                    if bb <= 0:
                                        bb = 0.0001
                                    xingjiabi.append((ADD16LIP_area[j] - ADD16LIP_area[0]) / bb)
                                    xingjiabiyuanlai.append('add16u_0EM')
                                    xingjiabihoulai.append(ADD16LIP[j])
                                    xingjiabijilu.append(4)
                                    xingjiabizengjia.append(j + 1)
                                    xingjiabiyuanlaiweizhi.append(i)
                                    cuowu.append(MEDerror)
                                if MEDerror > mubiaocuowu:
                                    xingjiabijilu.append(4)
                if (peizhi[i] == 2) & (obj['functions']['function'] == 'mul8u_150Q'):
                    if (int(5 in xingjiabijilu) == 0):
                        if len(MUL8LIPcuowu1) > 2:
                            for j in range(2, len(MUL8LIPcuowu1)):
                                obj['functions']['function'] = MUL8LIP[j]
                                MEDerror = computing.GAerror1(_listdangqiancopy)
                                bb = MEDerror - MED
                                if MEDerror <= mubiaocuowu:
                                    if bb <= 0:
                                        bb = 0.0001
                                    xingjiabi.append((MUL8LIP_area[j] - MUL8LIP_area[1]) / bb)
                                    xingjiabiyuanlai.append('mul8u_150Q')
                                    xingjiabihoulai.append(MUL8LIP[j])
                                    xingjiabijilu.append(5)
                                    xingjiabizengjia.append(j + 1)
                                    xingjiabiyuanlaiweizhi.append(i)
                                    cuowu.append(MEDerror)
                                if MEDerror > mubiaocuowu:
                                    xingjiabijilu.append(5)
                if (peizhi[i] == 2) & (obj['functions']['function'] == 'add16u_08F'):
                    if (int(6 in xingjiabijilu) == 0):
                        if len(ADD16LIPcuowu1) > 2:
                            for j in range(2, len(ADD16LIPcuowu1)):
                                obj['functions']['function'] = ADD16LIP[j]
                                MEDerror = computing.GAerror1(_listdangqiancopy)
                                bb = MEDerror - MED
                                if MEDerror <= mubiaocuowu:
                                    if bb <= 0:
                                        bb = 0.0001
                                    xingjiabi.append((ADD16LIP_area[j] - ADD16LIP_area[1]) / bb)
                                    xingjiabiyuanlai.append('add16u_08F')
                                    xingjiabihoulai.append(ADD16LIP[j])
                                    xingjiabijilu.append(6)
                                    xingjiabizengjia.append(j + 1)
                                    xingjiabiyuanlaiweizhi.append(i)
                                    cuowu.append(MEDerror)
                                if MEDerror > mubiaocuowu:
                                    xingjiabijilu.append(6)

            for i in range(0, len(xingjiabi)):
                for j in range(0, len(xingjiabi) - 1):
                    if xingjiabi[j] < xingjiabi[j + 1]:
                        a = xingjiabi[j]
                        b = xingjiabiyuanlai[j]
                        c = xingjiabihoulai[j]
                        d = xingjiabijilu[j]
                        e = xingjiabizengjia[j]
                        f = xingjiabiyuanlaiweizhi[j]
                        xingjiabi[j] = xingjiabi[j + 1]
                        xingjiabiyuanlai[j] = xingjiabiyuanlai[j + 1]
                        xingjiabihoulai[j] = xingjiabihoulai[j + 1]
                        xingjiabijilu[j] = xingjiabijilu[j + 1]
                        xingjiabizengjia[j] = xingjiabizengjia[j + 1]
                        xingjiabiyuanlaiweizhi[j] = xingjiabiyuanlaiweizhi[j + 1]
                        xingjiabi[j + 1] = a
                        xingjiabiyuanlai[j + 1] = b
                        xingjiabihoulai[j + 1] = c
                        xingjiabijilu[j + 1] = d
                        xingjiabizengjia[j + 1] = e
                        xingjiabiyuanlaiweizhi[j + 1] = f
            #When the array is empty, find the depth again and judge it again
            if len(xingjiabiyuanlai)==0:
                        depth=0

    return xingjiabi, xingjiabiyuanlai, xingjiabihoulai, xingjiabijilu, xingjiabizengjia, xingjiabiyuanlaiweizhi,depth
