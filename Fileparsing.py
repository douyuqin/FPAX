import copy
import re

import computing
import confirandcompu


ii = 0


class RegMatch(object):
    def __init__(self):
        self.data = ''
        self.operations = []
        self.json_body = []

    def load_txt(self):
        with open("applications/conv3x3.cdfg", "r") as f:
            self.data = f.read()

    def format_data(self):
        # 正则匹配以operation开头  }结尾
        # reg = '(?<=operation).+?(?=})'
        reg = 'operation.+?}'
        self.operations = re.findall(reg, self.data, re.DOTALL)
        for obj in self.operations:
            # self.format_operation(obj)
            self.json_body.append(self.format_operation(obj))

    def format_operation(self, str):
        # func_reg = '(?<=function ).+?(?=;)'
        # func_name = re.findall(func_reg, str)[0]
        opera_reg = '[(](.*?)[)]'
        opera_name = re.findall(opera_reg, str)[0]

        func_body_reg = '[{](.*?)[}]'
        func_body = re.findall(func_body_reg, str, re.DOTALL)
        func_body = func_body[0].replace("\n", "").replace('\t', '')
        func_body_list = func_body.split(";")
        func_body_dic = {}

        for obj in func_body_list:
            if len(obj):
                obj_list = obj.split(" ")
                # 如果有多个值
                if ',' in obj_list[1]:
                    paras = obj_list[1].split(",")
                    func_body_dic[obj_list[0]] = paras
                else:
                    if obj_list[0] == 'read':
                        # 如果是read  全部使用数组
                        func_body_dic[obj_list[0]] = [obj_list[1]]
                    else:
                        func_body_dic[obj_list[0]] = obj_list[1]
        func_body_dic['write_data'] = [0 for i in range(1)]

        # 生成全0的数组 用于记录多个read值
        order_list = [0 for i in range(len(func_body_dic['read']))]
        return {
            'opera_name': opera_name,
            'functions': func_body_dic,
            'order': 0,
            'order_list': order_list
        }

    # 进行排序
    def search_order(self):
        for i in range(len(self.json_body)):
            obj = self.json_body[i]
            target = obj['functions']['write']

            # 获取write的层次排序
            order_list = []
            for j in range(len(obj['functions']['read'])):
                level = self.get_level(obj['functions']['read'][j], 0)
                order_list.append(level)

            obj['order_list'] = order_list
            # 依赖 单个依赖 多个依赖
            obj['depend_list'] = self.depend_array(obj['functions']['read'])

        for i in range(len(self.json_body)):
            obj = self.json_body[i]
            obj['order'] = max(obj['order_list'])

        print(self.json_body)
        return self.json_body

    def depend_array(self, _target: list) -> list:
        depend_count = 0
        ret_list = []
        for j in range(len(_target)):
            # read 值
            _read = _target[j]

            for i in range(len(self.json_body)):
                obj = self.json_body[i]
                if obj['functions']['write'] == _read:
                    depend_count += 1
                    break
        if not depend_count:
            # 没有找到依赖
            ret_list = [2, 2]
        if depend_count == 1:
            # 只有一个依赖
            ret_list = [3, 1]
        elif depend_count == 2:
            # 两个依赖
            ret_list = [3, 3]
        return ret_list

    def get_level(self, _targe, level):
        '''
        递归寻找
        @param _targe: 寻找层次的目标 write
        @param level: 层次
        @param has_searched: 已经寻找过的数组
        @return:
        '''
        for i in range(len(self.json_body)):
            obj = self.json_body[i]
            # 如果找到了
            if obj['functions']['write'] == _targe:
                # 异常判断
                if isinstance(obj['functions']['read'], list):
                    read_list = obj['functions']['read']
                    # level_list = obj['order_list']
                    level_list = []
                    # 这里进行深度遍历
                    for j in range(len(read_list)):
                        # 继续查询 read 数组
                        ret_level = self.get_level(read_list[j], level + 1)
                        level_list.append(ret_level)
                    return max(level_list)
                    #  持久化
                    # obj['order_list'] = level_list
                else:
                    return level
        # 没找到
        return level


reg = RegMatch()
reg.load_txt()
reg.format_data()
_list = reg.search_order()
