import copy

MUL8LIP = ['mul8u_EXZ', 'mul8u_150Q', 'mul8u_CK5']
MUL8LIP_area = [11, 31, 46]
ADD16LIP = ['add16u_0EM', 'add16u_08F', 'add16u_1JH']
ADD16LIP_area = [15, 20, 21]

def make(depth, n, _listdangqian, xingjiabizengjia, xingjiabiyuanlai, xingjiabihoulai,peizhi):


    sum = 0
    zengjiaweizhi = []
    zengjiachengdu = []
    # find depth
    _listdangqiancopy1 = copy.deepcopy(_listdangqian)
    if len(xingjiabiyuanlai) < 2:
        for j in range(0,2):
            if len(zengjiaweizhi) == 0:
                for i in range(depth-1, len(_listdangqiancopy1)):
                    obj = _listdangqiancopy1[i]
                    if obj['functions']['function'] == xingjiabiyuanlai[0]:
                        obj['functions']['function'] = 'sra'
                        zengjiaweizhi.append(i)
                        zengjiachengdu.append(xingjiabizengjia[0])
                        sum = sum + xingjiabizengjia[0]
                        if sum >= n:
                            break
                if len(zengjiaweizhi) == 0:
                    depth=depth-1


    zengjiaweizhi1 = []
    zengjiachengdu1 = []
    sum=0
    _listdangqiancopy2 = copy.deepcopy(_listdangqian)
    if len(xingjiabiyuanlai) >= 2:
        # print('zengjiaweizhi1', 55)
        for i in range(depth-2, len(_listdangqiancopy2)):
            obj = _listdangqiancopy2[i]
            if obj['functions']['function'] == xingjiabiyuanlai[0]:
                obj['functions']['function'] = 'sra'
                zengjiaweizhi1.append(i)
                zengjiachengdu1.append(xingjiabizengjia[0])
                sum = sum + xingjiabizengjia[0]
                if sum >= n:
                    break
        if sum < n:
            for i in range(depth-2, len(_listdangqiancopy2)):
                obj = _listdangqiancopy2[i]
                if obj['functions']['function'] == xingjiabiyuanlai[1]:
                    obj['functions']['function'] = 'sra'
                    zengjiaweizhi1.append(i)
                    zengjiachengdu1.append(xingjiabizengjia[1])
                    sum = sum + xingjiabizengjia[1]
                    if sum >= n:
                        break


    zengjiaweizhi2 = []
    zengjiachengdu2 = []
    sum=0
    _listdangqiancopy3 = copy.deepcopy(_listdangqian)
    if len(xingjiabiyuanlai) >= 2:
        for i in range(depth-2, len(_listdangqiancopy3)):
            obj = _listdangqiancopy3[i]
            if obj['functions']['function'] == xingjiabiyuanlai[1]:
                obj['functions']['function'] = 'sra'
                zengjiaweizhi2.append(i)
                zengjiachengdu2.append(xingjiabizengjia[1])
                sum = sum + xingjiabizengjia[1]
                if sum >= n:
                    break
        if sum < n:
            for i in range(depth-2, len(_listdangqiancopy3)):
                obj = _listdangqiancopy3[i]
                if obj['functions']['function'] == xingjiabiyuanlai[0]:
                    obj['functions']['function'] = 'sra'
                    zengjiaweizhi2.append(i)
                    zengjiachengdu2.append(xingjiabizengjia[0])
                    sum = sum + xingjiabizengjia[0]
                    if sum >= n:
                        break


    peizhireducezuizhong = []
    depthrecord=[]
    if len(xingjiabiyuanlai) >= 2:
        for i in range(0, len(zengjiaweizhi2)):
            peizhireduce = copy.deepcopy(peizhi)
            if i > 0:
                for z in range(0, i):
                    peizhireduce[zengjiaweizhi2[z]] = zengjiachengdu2[z]
                    a=0
                for a in range(i, len(zengjiaweizhi1) - i):
                    peizhireduce[zengjiaweizhi1[a]] = zengjiachengdu1[a]
                if a>0: #有可能zengjiaweizhi1的值为空
                    b=zengjiaweizhi1[a]
                else:
                    b = zengjiaweizhi2[z]

            else:
                for j in range(0, len(zengjiaweizhi1)):
                    peizhireduce[zengjiaweizhi1[j]] = zengjiachengdu1[j]
                b = zengjiaweizhi1[j]

            peizhireducezuizhong.append(peizhireduce)
            depthrecord.append(b)
    if len(xingjiabiyuanlai) < 2:
        peizhireduce = copy.deepcopy(peizhi)
        for j in range(0, len(zengjiaweizhi)):
            peizhireduce[zengjiaweizhi[j]] = zengjiachengdu[j]
        a = zengjiaweizhi[j]
        peizhireducezuizhong.append(peizhireduce)
        depthrecord.append(a)

    return peizhireducezuizhong, depthrecord
