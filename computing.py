import random
import numpy as np
import copy

from applications import laplacecomputing, fircomputing, convcomputing, conv,sobelcomputng


def GAerror1(_list):
    MED = conv.convverrorcomputing(_list)
    return MED