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

# copyright (c) Laurent Claessens, 2010-2016
# email: laurent@claessens-donadello.eu

from phystricks.ObjectGraph import ObjectGraph
from Constructors import *
from Utilities import *

class FractionPieDiagramGraph(ObjectGraph):
    def __init__(self,center,radius,a,b):
        """
        The pie diagram for the fraction 'a/b' inside the circle of given center and radius.

        2/4 and 1/2 are not treated in the same way because 2/4 divides the pie into 4 parts (and fills 2) while 1/2 divides into 2 parts.
        """
        ObjectGraph.__init__(self,self)
        self.center=center
        self.radius=radius
        self.numerator=a
        self.denominator=b
        if a>b:
            raise ValueError,"Numerator is larger than denominator"
        self.circle=Circle(self.center,self.radius)
        self._circular_sector=None
    def circular_sector(self):
        if not self._circular_sector :
            FullAngle=AngleMeasure(value_degree=360)
            cs=CircularSector(self.center,self.radius,0,self.numerator*FullAngle//self.denominator)
            cs.parameters.filled()
            cs.parameters.fill.color="lightgray"
            self._circular_sector=cs
        return self._circular_sector
    def bounding_box(self,pspict):
        return self.circle.bounding_box(pspict)
    def latex_code(self,language=None,pspict=None):
        return ""
    def specific_action_on_pspict(self,pspict):
        raise
        if self.denominator==self.numerator:
            cs=Circle(self.center,self.radius)
            cs.parameters.filled()
            cs.parameters.fill.color="lightgray"
            l=[cs]
        else :
            import numpy
            l=[self.circular_sector()]
            for k in numpy.linspace(0,360,self.denominator,endpoint=False):
                s=Segment(  self.circle.get_point(k),self.center  )
                s.parameters.style="dashed"
                l.append(s)
            l.append(self.circle)
        pspict.DrawGraphs(l)

