#! /usr/bin/sage -python
# -*- coding: utf8 -*-

import sys
from phystricks import *

from phystricksOnePoint import OnePoint
from phystricksRJDEoobOibtkfv import RJDEoobOibtkfv
from phystricksLARGooSLxQTdPC import LARGooSLxQTdPC
from phystricksPBFCooVlPiRBpt import PBFCooVlPiRBpt
from phystricksGKMEooBcNxcWBt import GKMEooBcNxcWBt
from FunctionThird import FunctionThird
from phystricksVSJOooJXAwbVEt import VSJOooJXAwbVEt
from phystricksIllusionNHwEtp import IllusionNHwEtp

figures_list_1=[]
figures_list_2=[]
figures_list_3=[]

def append_picture(fun,number):
    figures_list_1.append(fun)
    if number>=2 :
        figures_list_2.append(fun)
    if number>=3 :
        figures_list_3.append(fun)

append_picture(RJDEoobOibtkfv,3)
append_picture(OnePoint,2)
append_picture(FunctionThird,2)
append_picture(GKMEooBcNxcWBt,2)
append_picture(LARGooSLxQTdPC,2)
append_picture(PBFCooVlPiRBpt,2)
append_picture(VSJOooJXAwbVEt,2)
append_picture(IllusionNHwEtp,1)
"""
append_picture(<++>,1)
append_picture(<++>,1)
append_picture(<++>,1)
append_picture(<++>,1)
append_picture(<++>,1)
"""


def AllFigures():
    figures_list=figures_list_1
    if "--pass-number=2" in sys.argv :
        figures_list=figures_list_2
    if "--pass-number=3" in sys.argv :
        figures_list=figures_list_3

    tests=FigureGenerationSuite(figures_list,first=0,title=u"phystricks's manual")
    tests.generate()
    tests.summary()

if __name__=="__main__":
    AllFigures()
