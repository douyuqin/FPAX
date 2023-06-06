import copy
import initialization
from producepeizhi import produce
import reducesimple
MUL8LIP = ['mul8u_EXZ', 'mul8u_150Q', 'mul8u_CK5']
MUL8LIP_area = [11, 31, 46]
ADD16LIP = ['add16u_0EM', 'add16u_08F', 'add16u_1JH']
ADD16LIP_area = [15, 20, 21]

def smartconfigure(_list,peizhi, n, tarError,depth):

    _lista = copy.deepcopy(_list)  #
    _listb = copy.deepcopy(_list)
    N = len(_lista)
    # Filter available approximation units for the current approximation configuration. Output errors for the current approximate configuration（curerror）
    (MUL8LIPcuowu1,ADD16LIPcuowu1,_listdangqian,curerror)=initialization.filterunit(_lista, N, peizhi, tarError)
    if (tarError - curerror) >=0:
    # inrease approximation units
        (output,outputenergy,error,depth,exit)=produce(depth, peizhi, MUL8LIPcuowu1, ADD16LIPcuowu1, tarError, n, _listdangqian, curerror, _list,N)
    if (tarError - curerror) < 0:
        # reduce approximation units
        (output,outputenergy,error,depth,exit)=reducesimple.reducesingle(output,peizhi,_listb,N,tarError)
    if (tarError - error) < 0:
        # reduce approximation units
        (output,outputenergy,error,depth,exit)=reducesimple.reducesingle(output,peizhi,_listb,N,tarError)
    return output,outputenergy,error,depth,exit

#output: Output Approximate Configuration
#outputenergy:Approximate configuration power savings
#depth：Depth of current configuration
#exit: Determine whether the cycle can be terminated