#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：demo_01 
@File ：nn.py
@Author ：SunKe
@Contact : 467358186
@Date ：2022/10/25 15:21
@Desc : 
'''

import re
import time
import copy

import random

import psutil as psutil
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.tensorboard import SummaryWriter
import pandas as pd
import numpy as np
from ast import literal_eval
from sklearn.model_selection import train_test_split

# import GAmedcomputing
# import shibiesobelwenjian
# import shujupeizhi
# import translearingsearch
import computing
import Fileparsing


train_file_name = ''
transfer_file_name = ''
verify_file_name = ''


class NNModel(nn.Module):
    def __init__(self):
        super(NNModel, self).__init__()
        self.fc1 = nn.Linear(1, 8)
        self.fc2 = nn.Linear(8, 8)
        self.fc3 = nn.Linear(8, 16)
        self.fc4 = nn.Linear(16, 4)
        self.fc5 = nn.Linear(4, 1)

    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)

        x = self.fc2(x)
        x = F.relu(x)

        x = self.fc3(x)
        x = F.relu(x)

        x = self.fc4(x)
        x = F.relu(x)

        x = self.fc5(x)
        return x


def load_data(modify=False, transfer=False, verify=False):
    # 数据
    global train_file_name
    global transfer_file_name
    global verify_file_name
    file_name = ''
    if modify:
        file_name = train_file_name
    if transfer:
        file_name = transfer_file_name
    if verify:
        file_name = verify_file_name

    with open(file_name) as f2:
        lines = f2.readlines()

    line = 0
    data = []  # 前两组数据
    target = []  # 结果
    for i in lines:
        if line % 2 == 0:
            data.append(float(i))
        else:
            target.append(float(i))
        line += 1
    if verify:
        # 验证
        return torch.Tensor(data), torch.Tensor(target)

    X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=101, test_size=0.1)
    x_train = torch.Tensor(np.array(X_train))
    y_train = torch.Tensor(np.array(y_train))
    X_test = torch.Tensor(np.array(X_test))
    y_test = torch.Tensor(np.array(y_test))
    return x_train, y_train, X_test, y_test


def train_model():
    x_train, y_train, x_test, y_test = load_data(modify=True)

    model = NNModel()

    epoch_n = 20
    learning_rate = 0.00001
    loss_f = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    # 训练
    loss_train_list = []
    loss_test_list = []

    for epoch in range(epoch_n):
        loss_test_epoch = []
        for i in range(x_train.shape[0]):
            optimizer.zero_grad()  # 将梯度设为0
            pred = model(torch.tensor(x_train[i], dtype=torch.float).unsqueeze(dim=0))
            loss_train = loss_f(pred, y_train[i])
            loss_train.backward()  # 反向传播
            optimizer.step()

            # test
        for i in range(x_test.shape[0]):
            pred = model(torch.tensor(x_test[i], dtype=torch.float).unsqueeze(dim=0))
            loss_test = loss_f(pred, y_test[i])
            loss_test_epoch.append(loss_test.detach().numpy())
        loss_test_epoch = np.array(loss_test_epoch)
        print('Epoch: ', epoch, '| train loss: %.4f' % np.mean(loss_test_epoch))
    torch.save(model.state_dict(), './model.pt')


def load_pt():
    x_train, y_train, X_test, y_test = load_data(transfer=True)
    model = NNModel()
    model.load_state_dict(torch.load('./model.pt'))
    pred = model(X_test)
    pred = torch.squeeze(pred)
    loss_f = torch.nn.MSELoss()
    loss_test = loss_f(pred, y_test)
    print(loss_test)  # 0.1629



# def transfer_pt():
#     x_train, y_train, x_test, y_test = load_data(transfer=True)
#
#     model = NNModel()
#     model.load_state_dict(torch.load('./model.pt'))
#     # model.fc1 = nn.Linear(input_dim, 16)
#
#
#     epoch_n = 20
#     learning_rate = 0.00001
#     loss_f = torch.nn.MSELoss()
#     optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
#     # 训练
#     for epoch in range(epoch_n):
#         loss_test_epoch = []
#         for i in range(x_train.shape[0]):
#             optimizer.zero_grad()  # 将梯度设为0
#             pred = model(torch.tensor(x_train[i], dtype=torch.float).unsqueeze(dim=0))
#             loss_train = loss_f(pred, y_train[i])
#             loss_train.backward()  # 反向传播
#             optimizer.step()
#
#             # test
#         for i in range(x_test.shape[0]):
#             pred = model(torch.tensor(x_test[i], dtype=torch.float).unsqueeze(dim=0))
#             loss_test = loss_f(pred, y_test[i])
#             loss_test_epoch.append(loss_test.detach().numpy())
#         loss_test_epoch = np.array(loss_test_epoch)
#         print('Epoch: ', epoch, '| train loss: %.4f' % np.mean(loss_test_epoch))
#     torch.save(model.state_dict(), './model_second.pt')

# 验证网络
def verify(x_test):
    # 加载网络
    loss_f = torch.nn.MSELoss()
    model = NNModel()
    # model.load_state_dict(torch.load('./model_second.pt'))
    model.load_state_dict(torch.load('./model.pt')) #Read NN
    # model = torch.load('./model.pt')
    pred = model(torch.tensor(x_test, dtype=torch.float).unsqueeze(dim=0))
    print(pred)
    return pred.detach().numpy()

