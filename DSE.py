import copy
import time
import psutil
import computing
import Fileparsing
from nn import verify
from smartconfirgation import smartconfigure

_list = Fileparsing._list  # Read an application
N = len(_list)  # Number of nodes in the application
tarError = 15.1  # Target Error
peizhi = [0]*N #Generate initial configuration
# Get maximum error
_list1=copy.deepcopy(_list)
print(peizhi)
for i in range(0,len(_list1)):
    obj = _list1[i]
    if obj['functions']['function'] == 'add':
        obj['functions']['function']='add16u_1JH'
    if obj['functions']['function'] == 'mul':
        obj['functions']['function']='mul8u_CK5'
obj1=_list1
MAXerror=computing.GAerror1(obj1)  #maximum error
mem = psutil.virtual_memory()
m1 = mem.used

x = 0
y = 0
x1 = 0  # Used to store the last error, fine-grained exploration requires
flag = 0
J1=2/MAXerror #fine-grained exploration requires
J2 = tarError/MAXerror # For the first exploration
Q=10 #Iterations
Z=N*3 #TAL
start_time = time.time()

# Coarse grain prediction
file_handle = open('shiyan/conv15.txt', mode='w')
for v in range(0, Q):

    if v == 0:
        n = verify(J2)
        depth = 0
    else:
        n = verify(x)
        depth = y
    n[0] = n[0] * Z
    n[0] = int(round(n[0]))
    _lista = copy.deepcopy(_list)  # 复制未改变的配置后面使用
    _listb = copy.deepcopy(_list)
    #Fine-grained prediction
    if (x < J1) & (v > 0):
        n[0] = 2
    (output, outputarea, error, depth, tuichu) = smartconfigure(_list, peizhi, n[0], tarError, depth)
    print(output, outputarea, error, depth)
    x = abs(tarError - error) / MAXerror
    y = depth
    peizhi = output
    end_time = time.time()
    print('v', v, (end_time - start_time))
    mem = psutil.virtual_memory()
    m2 = mem.used
    t2 = time.time()
    file_handle.write(str(v) + '\n')
    file_handle.write(str(output) + '\n')
    file_handle.write(str(outputarea) + '\n')
    file_handle.write(str(error) + '\n')
    file_handle.write(str('time') + '\n')
    file_handle.write(str((end_time - start_time)) + '\n')
    file_handle.write(str('mem') + '\n')
    file_handle.write(str((m2 - m1)/(1024*1024)) + '\n')
    if (x1 > tarError) & (error <= tarError):
        flag = flag + 1
        if flag == 2:
            break
    else:
        x1 = error
    if tuichu > 0:
        break