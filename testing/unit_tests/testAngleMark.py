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

# copyright (c) Laurent Claessens, 2017
# email: laurent@claessens-donadello.eu

from __future__ import division

from phystricks import *

from Testing import assert_true
from Testing import assert_false
from Testing import assert_equal
from Testing import assert_almost_equal
from Testing import echo_function
from Testing import echo_single_test
from Testing import SilentOutput

def create_example(angleI,angleF,text,name,dist=None):
    pspict,fig = SinglePicture("AngleTest"+name)

    O=Point(0,0)
    Cer=Circle(O,2)
    A=Cer.get_point(angleI)
    B=Cer.get_point(angleF)
    seg1=Segment(O,A)
    seg2=Segment(O,B)

    angle=AngleAOB(A,O,B)

    angle.put_mark(dist=dist,text=text,pspict=pspict)

    pspict.DrawGraphs(angle)
    return angle,pspict

def testAngleMark():
    echo_function("testAngleMark")

    print("remettre le SilentOutput")

    with SilentOutput() :
        angle,pspict = create_example(angleI=160,angleF=223,text="\( \int_A40mmmm\)",name="Six",dist=None)

    mark=angle.added_objects[pspict][0]
    code=mark.tikz_code()

    # this is not the correct final answer because
    # it depends on the position in the picture (size of the box)
    # I'm testing here if something in the processus is indeterministic.
    ans="\draw (-0.6170939622,-0.1216103571) node {\( \int_A40mmmm\)};"

    assert_equal(code,ans)
