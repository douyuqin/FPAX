import computing
import confirandcompu
MUL8LIP = ['mul8u_EXZ', 'mul8u_150Q', 'mul8u_CK5']
MUL8LIP_area = [11, 31, 46]
ADD16LIP = ['add16u_0EM', 'add16u_08F', 'add16u_1JH']
ADD16LIP_area = [15, 20, 21]

def filterunit(_lista,N,peizhi,mubiaocuowu): # Filter available approximation units for the current approximation configuration

    (ADD16LIPcuowu, MUL8LIPcuowu) = confirandcompu.singleapproximate(_lista, _lista, N, 100)
    (_listdangqian, sum1) = confirandcompu.confirgure(_lista, peizhi, N)  # 根据配置改变应用
    error = computing.GAerror1(_listdangqian)  # 计算当前配置的MED
    # Filter approximation units
    MUL8LIPcuowu1 = []
    for i in range(0, len(MUL8LIPcuowu)):
        if abs(error - mubiaocuowu) > 3.5:
            if MUL8LIPcuowu[i] < abs(error - mubiaocuowu):
                MUL8LIPcuowu1.append(MUL8LIPcuowu[i])
        if abs(error - mubiaocuowu) <= 3.5:
            if MUL8LIPcuowu[i] <= 3.5:
                MUL8LIPcuowu1.append(MUL8LIPcuowu[i])
    ADD16LIPcuowu1 = []
    for i in range(0, len(ADD16LIPcuowu)):
        if abs(error - mubiaocuowu) > 3.5:
            if abs(error - mubiaocuowu) > 3.5:
                if ADD16LIPcuowu[i] < abs(error - mubiaocuowu):
                    ADD16LIPcuowu1.append(ADD16LIPcuowu[i])
        if abs(error - mubiaocuowu) <= 3.5:
            if MUL8LIPcuowu[i] <= 3.5:
                ADD16LIPcuowu1.append(ADD16LIPcuowu[i])
    return MUL8LIPcuowu1,ADD16LIPcuowu1,_listdangqian,error