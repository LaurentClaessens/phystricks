# -*- coding: utf8 -*-

###########################################################################
#   This is part of the module phystricks
#
#   phystricks is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   phystricks is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with phystricks.py.  If not, see <http://www.gnu.org/licenses/>.
###########################################################################

# copyright (c) Laurent Claessens, 2016
# email: laurent@claessens-donadello.eu

from sage.all import *

from ObjectGraph import ObjectGraph
from Constructors import *

class LeftMatrixBraceGraph(ObjectGraph):
    def __init__(self,P,Q,r1,r2):
        ObjectGraph.__init__(self,self)
        self.P=P
        self.Q=Q
        self.r1=r1
        self.r2=r2
    def action_on_pspict(self,pspict):
        s=Segment(self.P,self.Q)
        C1=s.get_point_length(self.r2)
        circle1=Circle(C1,self.r).graph(s.angle()+180,s.angle()+180+90)

        C2=s.get_point_length( s.length()-self.r )
        circle2=Circle(C2,self.r).graph(s.angle(),s.angle()-90)

        I=circle1.getPoint(circle1.angleF)
        F=circle2.getPoint(circle2.angleF)
        border=Segment(I,F)

        pspict.DrawGraphs(circle1,circle2,border)
