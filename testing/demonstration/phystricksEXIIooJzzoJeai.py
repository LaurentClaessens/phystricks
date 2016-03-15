# -*- coding: utf8 -*-
from phystricks import *
def EXIIooJzzoJeai():
    pspicts,fig = MultiplePictures("EXIIooJzzoJeai",4)
    pspicts[0].mother.caption="Normal (50 points)"
    pspicts[1].mother.caption="with force smoothing"
    pspicts[2].mother.caption="adding smart plotpoints"
    pspicts[3].mother.caption="more points (1000)"

    xmin=0.05
    x=var('x')
    f1=phyFunction( sin(1/x)  ).graph(xmin,6)
    f2=phyFunction( sin(1/x)  ).graph(xmin,6)
    f3=phyFunction( sin(1/x)  ).graph(xmin,6)
    f4=phyFunction( sin(1/x)  ).graph(xmin,6)

    for psp in pspicts:
        psp.dilatation_X(1)
        psp.dilatation_Y(1)

    f2.curvature_plotpoints=50
    f3.added_plotpoints=[2/(k*pi) for k in range(1,13)]  
    f4.plotpoints=1000

    pspicts[0].DrawGraphs(f1)
    pspicts[1].DrawGraphs(f2)
    pspicts[2].DrawGraphs(f3)
    pspicts[3].DrawGraphs(f4)

    for psp in pspicts:
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
