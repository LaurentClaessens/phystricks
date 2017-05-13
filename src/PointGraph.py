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

# copyright (c) Laurent Claessens, 2010-2017
# email: laurent@claessens-donadello.eu

from __future__ import division
from __future__ import unicode_literals

from sage.all import *

from ObjectGraph import ObjectGraph
from Constructors import *
from Utilities import *
from MathStructures import *

class PointGraph(ObjectGraph):
    def __init__(self,a,b):
        self.x=SR(a)
        self.y=SR(b)
        ObjectGraph.__init__(self,self)
        self.point = self.obj
        self.add_option("PointSymbol=*")
        self._advised_mark_angle=None
        
        ax=abs(numerical_approx(self.x))
        if ax<0.00001 and ax>0 :
            self.x=0
        ay=abs(numerical_approx(self.y))
        if ay<0.00001 and ay>0 :
            self.y=0

    def advised_mark_angle(self,pspict):
        if self._advised_mark_angle is None :
            self._advised_mark_angle=self.angle()
        return self._advised_mark_angle
    def numerical_approx(self):
        return Point(numerical_approx(self.x),numerical_approx(self.y))
    def projection(self,seg,direction=None,advised=False):
        """
        Return the projection of the point on the given segment.

        INPUT:

        - ``seg`` - a segment
        - ``direction`` - (default=None) a vector.
        If given, we use a projection parallel to 
        `vector` instead of the orthogonal projection.

        OUTPUT:

        a point.

        EXAMPLES:

        Return a point even if the projections happens
        to lies outside the segment::

            sage: from phystricks import *
            sage: s1=Segment( Point(0,0),Point(2,1) )
            sage: print Point(3,-1).projection(s1)
            <Point(2,1)>
            sage: print Point(5,0).projection(s1) 
            <Point(4,2)>

        You can project on a vector::

            sage: print Point(5,0).projection(Vector(2,1))
            <Point(4,2)>
        """
        from AffineVectorGraph import AffineVectorGraph
        from SingleAxeGraph import SingleAxeGraph
        if isinstance(seg,AffineVectorGraph):
            seg=seg.segment
        if isinstance(seg,SingleAxeGraph):
            seg=seg.segment()
        if direction is None:
            if seg.vertical :
                direction=Segment(  self, self+( 1,0  )  )
            elif seg.horizontal :
                direction=Segment(self,self+(0,1))
            else :
                direction=Segment(  self, self+(  1,-1/seg.slope    )  )

        P=Intersection(seg,direction)[0]
        if advised :
            P._advised_mark_angle=seg.angle().degree+90
        return P
    def symmetric_by(self,Q):
        """
        return the central symmetry  with respect to 'Q'
        """
        v=Q-self
        return Q+v
    def getPolarPoint(self,r,theta,pspict=None):
        """
        Return the point located at distance r and angle theta from point self.

        INPUT:

        - ``r`` - A number.

        - ``theta`` - the angle (degree or :class:`AngleMeasure`).

        - ``pspict`` - the pspicture in which the point is supposed to live. If `pspict` is given, we compute the deformation due to the dilatation.  Be careful: in that case `r` is given as absolute value and the visual effect will not be affected by dilatations.

        OUTPUT: A point.

        EXAMPLES::

            sage: from phystricks import *
            sage: P=Point(1,2)
            sage: print P.get_polar_point(sqrt(2),45)
            <Point(2,3)>

        """
        if isinstance(r,AngleMeasure):
            raise ShouldNotHappenException("You are passing AngleMeasure instead of a number (the radius).")
        if isinstance(theta,AngleMeasure):
            alpha=theta.radian
        else :
            alpha=radian(theta,number=True)
        if pspict:
            A=pspict.xunit
            B=pspict.yunit
            xP=r*cos(alpha)/A
            yP=r*sin(alpha)/B
            return self.translate(Vector(xP,yP))
        return Point(self.x+r*cos(alpha),self.y+r*sin(alpha))
    def get_polar_point(self,r,theta,pspict=None):
        return self.getPolarPoint(r,theta,pspict)
    def getVisualPolarPoint(self,r,theta,pspict=None):
        from SmallComputations import visualPolarCoordinates
        xunit=1
        yunit=1
        if pspict:
            xunit=pspict.xunit
            yunit=pspict.yunit
        rp,alpha=visualPolarCoordinates(r,theta,xunit=xunit,yunit=yunit)
        rp,alpha=visualPolarCoordinates(r,theta,xunit=xunit,yunit=yunit)
        P = self.getPolarPoint(rp,alpha)
        return self.getPolarPoint(rp,alpha)
    def rotation(self,alpha):
        """
        return a point that is the rotation of 'self' by the angle 'alpha'

        - alpha : the rotation angle (degree)
        """
        pc=self.polar_coordinates()
        return PolarPoint(pc.r,pc.degree+alpha)
    def value_on_line(self,line):
        """
        Return the value of the equation of a line on `self`.

        If $f(x,y)=0$ is the equation of `line`, return the number f(self.x,self.y).

        NOTE:

        The object `line` has to have an attribute line.equation

        EXAMPLE::

            sage: from phystricks import *
            sage: s=Segment(Point(0,1),Point(1,0))
            sage: s.equation()
            x + y - 1 == 0
            sage: P=Point(-1,3)
            sage: P.value_on_line(s)
            1   

        It allows to know if a point is inside or outside a circle::

            sage: circle=Circle(Point(-1,2),4)
            sage: Point(1,1).value_on_line(circle)
            -11

        ::

            sage: Point(1,sqrt(2)).value_on_line(circle)
            (sqrt(2) - 2)^2 - 12

        """
        x,y=var('x,y')
        return line.equation.lhs()(x=self.x,y=self.y)
    def translate(self,a,b=None):
        """
        translate `self`.

        EXAMPLES::

        You can translate by a :func:`Vector`::

            sage: from phystricks import *
            sage: v=Vector(2,1)                        
            sage: P=Point(-1,-1)
            sage: print P.translate(v)
            <Point(1,0)>

        An :func:`AffineVector` is accepted::

            sage: w=AffineVector( Point(1,1),Point(2,3) )
            sage: print P.translate(w)
            <Point(0,1)>

        You can also directly provide the coordinates::

            sage: print P.translate(10,-9)
            <Point(9,-10)>

        Or the :func:`Point` corresponding to the translation vector::

            sage: print P.translate( Point(3,4)  )
            <Point(2,3)>

        Translation by minus itself produces zero::

            sage: x,y=var('x,y')
            sage: P=Point(x,y)
            sage: print P.translate(-P)
            <Point(0,0)>

        """
        if b==None :
            v=a
        else :
            v=Vector(a,b)
        return self+v
    def origin(self,P):
        """
        Let S be the point self.

        Return the affine vector   PK
        where K is such that   PK=OS

        In other words, it return the affine vector O->self but
        attached on point P instead of O.
        """
        return AffineVector(P,Point(P.x+self.x,P.y+self.y))
    def Vector(self):
        return AffineVector(Point(0,0),self)
    @lazy_attribute
    def norm(self):
        """
        Return the norm of the segment between (0,0) and self.

        This is the radial component in polar coordinates.

        EXAMPLES::

        sage: from phystricks import *
        sage: Point(1,1).norm()
        sqrt(2)
        sage: Point(-pi,sqrt(2)).norm()
        sqrt(pi^2 + 2)
        """
        return Segment(Point(0,0),self).length
    @lazy_attribute
    def length(self):
        """
        The same as self.norm()

        EXAMPLES::

            sage: from phystricks import *
            sage: P=Point(1,1)
            sage: P.length()
            sqrt(2)
        """
        return self.norm
    # La méthode normalize voit le point comme un vecteur partant de zéro, et en donne le vecteur de taille 1
    def normalize(self,l=None):
        """
        Return a vector of norm <l>. If <l> is not given, take 1.
        """
        unit = self*(1/self.norm)
        if l :
            return unit*l
        return unit
    def default_graph(self,opt):
        """
        Return a default Graph
        
        <opt> is a tuple. The first is the symbol to the point (like "*" or "none").
        The second is a string to be passed to pstricks, like "linecolor=blue,linestyle=dashed".
        """
        P=self.default_associated_graph_class()(self)
        P.parameters.symbol=opt[0]
        P.add_option(opt[1])
        return P
    def default_associated_graph_class(self):
        """Return the class which is the Graph associated type"""
        return PointGraph   
    def polar_coordinates(self,origin=None):
        """
        Return the polar coordinates of the point as a tuple (r,angle) where angle is AngleMeasure

        EXAMPLES::

            sage: from phystricks import *
            sage: Point(1,1).polar_coordinates()
            (sqrt(2), AngleMeasure, degree=45.0000000000000,radian=1/4*pi)
            sage: Point(-1,1).polar_coordinates()
            (sqrt(2), AngleMeasure, degree=135.000000000000,radian=3/4*pi)
            sage: Point(0,2).polar_coordinates()
            (2, AngleMeasure, degree=90.0000000000000,radian=1/2*pi)
            sage: Point(-1,0).polar_coordinates()
            (1, AngleMeasure, degree=180.000000000000,radian=pi)
            sage: alpha=-pi*(arctan(2)/pi - 2)
            sage: Point(cos(alpha),sin(alpha)).polar_coordinates()
            (1, AngleMeasure, degree=180.000000000000,radian=pi)

        If 'origin' is given, it is taken as origin of the polar coordinates.

        Only return positive angles (between 0 and 2*pi)
        """
        return PointToPolaire(self,origin=origin)
    def angle(self,origin=None):
        """
        Return the angle of the segment from (0,0) and self.

        Return type : MathStructure.AngleMeasure
        """
        return self.polar_coordinates(origin=origin).measure            # No more degree. February 11, 2015
    def coordinates(self,numerical=False,digits=None,pspict=None):
        """
        Return the coordinates of the point as a string.

        When one coordinate if very small (lower than 0.0001), it is rounded to zero in order to avoid string like "0.2335e-6" in the pstricks code.

        EXAMPLE::

            sage: from phystricks import *
            sage: P=Point(1,3)
            sage: print P.coordinates()
            sage: Q=Point(1,-pi)
            sage: print P.coordinates()
            (1,-pi)

        If a pspicture is given, we divide by xunit and yunit to normalize.
        """
        from Numerical import is_almost_zero
        x=self.x
        y=self.y
        if pspict :
            x=x*pspict.xunit
            y=y*pspict.yunit
            if pspict.rotation_angle is not None:
                ang=pspict.rotation_angle*pi/180
                nx=x*cos(ang)+y*sin(ang)
                ny=-x*sin(ang)+y*cos(ang)
                x=nx
                y=ny
        if digits :
            numerical=True
        if numerical :
            if digits==None :
                digits=10
            x=numerical_approx(x,digits=digits)
            y=numerical_approx(y,digits=digits)
        # Avoid something like "0.125547e-6" (LaTeX will not accept).
        if is_almost_zero(x,0.001):
            x=0
        if is_almost_zero(y,0.001):
            y=0
        return str("("+str(x)+","+str(y)+")")
    def graph_object(self):
        return PointGraph(self)
    def copy(self):
        return Point(self.x,self.y)
    def mark_point(self,pspict=None):
        return self
    def _bounding_box(self,pspict=None):
        """
        return the bounding box of the point including its mark

        A small box of radius 0.1 (modulo xunit,yunit[1]) is given in any case.
        You need to provide a pspict in order to compute the size since
        it can vary from the place in your document you place the figure.

        [1] If you dont't know what is the "bounding box", or if you don't wan
        t to fine tune it, you don't care.
        """
        if pspict==None:
            print("You should consider to give a Picture as argument. \
                    Otherwise the boundig box of %s could be bad"%str(self))
            xunit=1
            yunit=1
        else :
            xunit=pspict.xunit
            yunit=pspict.yunit
        Xradius=0.1/xunit
        Yradius=0.1/yunit
        bb = BoundingBox(Point(self.x-Xradius,self.y-Yradius),
                            Point(self.x+Xradius,self.y+Yradius))
        for P in self.record_add_to_bb:
            raise DeprecationWarning
            bb.AddPoint(P)
        for obj in self.added_objects[pspict]:
            bb.append(obj,pspict)
        return bb
    def _math_bounding_box(self,pspict=None):
        ##
        #   Return a bounding box which include itself and that's it.

        # Here one cannot use BoundingBox(self.point,self.point) because
        # it creates infinite loop.
        bb=BoundingBox(xmin=self.point.x,xmax=self.point.x,
                            ymin=self.point.y,ymax=self.point.y)
        return bb
    def is_almost_equal(self,other,epsilon=0.0001):
        ## 
        #   return true if `self` and `other` have coordinates difference
        #   lower than `epsilon`
        #

        if not isinstance(other,PointGraph):
            from NoMathUtilities import logging
            logging("We are comparing "+type(self)+" with "+type(other)+". We continue, but this is strange.")

        sx=numerical_approx(self.x)
        sy=numerical_approx(self.y)
        ox=numerical_approx(other.x)
        oy=numerical_approx(other.y)
        if abs(sx-ox)>epsilon:
            return False
        if abs(sy-oy)>epsilon:
            return False
        return True

    def tikz_code(self,pspict=None):
        symbol_dict={}
        symbol_dict[None]="$\\bullet$"
        symbol_dict["*"]="$\\bullet$"
        symbol_dict["|"]="$|$"
        symbol_dict["x"]="$\\times$"
        symbol_dict["o"]="$o$"
        symbol_dict["diamond"]="$\diamondsuit$"
        try :
            effective_symbol=symbol_dict[self.parameters.symbol]
        except KeyError:
            effective_symbol=self.parameters.symbol
        if self.parameters.symbol=='none' :
            from NoMathUtilities import logging
            logging("You should use '' instead of 'none'",pspict=pspict)
        if self.parameters.symbol not in ["none",""]:
            s = "\draw [{2}]  {0} node [rotate={3}] {{{1}}};".format(self.coordinates(numerical=True,pspict=pspict),effective_symbol,self.params(language="tikz",refute=["symbol","dotangle"]),"DOTANGLE")
            if self.parameters.dotangle != None :
                s=s.replace("DOTANGLE",str(self.parameters.dotangle))
            else :
                s=s.replace("DOTANGLE","0")
            return s
        return ""
    def latex_code(self,language=None,pspict=None,with_mark=False):
        l=[]

        if language=="tikz":
            l.append(self.tikz_code(pspict=pspict))
        return "\n".join(l)

    def __eq__(self,other):
        ##
        #        return True if the coordinates of `self` and `other` are the same.
        #
        #     INPUT:
        #        
        #        - ``other`` - an other point
        #
        #        OUTPUT:
        #
        #       boolean
        #
        #        This function tests exact equality (even symbolic if one needs). For
        #        numerical equality (up to some epsilon), use the function 
        #        `is_almost_equal`

        # The type verification is to avoid to get other.x
        # when comparing with an object that is completely different.
        # This happens when checking if the BB is already computed :
        # see also 13756-24006
        if not isinstance(other,PointGraph):
            return NotImplemented

        if self.x == other.x and self.y==other.y :
            return True
        return False
    def __add__(self,v):
        """
        Addition of a point with a vector is the parallel translation,
        while addition of a point with an other point is simply
        the addition of coordinates.

        INPUT:

        - ``v`` - a vector or a tuple of size 2

        OUTPUT:

        a new point
        """
        if isinstance(v,tuple) :
            if len(v)==2:
                return Point(self.x+v[0],self.y+v[1])
            else :
                raise TypeError, "Cannot sum %s with %s."%(self,v)
        try :
            dx = v.Dx
            dy = v.Dy
        except AttributeError :
            try :
                dx = v.x
                dy = v.y
            except AttributeError :
                print("VSWooXmhSzY")
                print(v.Dx())
                print(v.Dx)
                raise TypeError, "You seem to add myself with something which is not a Point neither a Vector. Sorry, but I'm going to crash : {},{}".format(v,type(v))
        return Point(self.x+dx,self.y+dy)
    def __sub__(self,v):
        if isinstance(v,tuple):
            if len(v)==2:
                return self+(-v[0],-v[1])
            else :
                raise TypeError, "Cannot sum %s with %s."%(self,v)
        return self+(-v)
    def __neg__(self):
        return Point(-self.x,-self.y)
    def __mul__(self,r):
        return Point(r*self.x,r*self.y)
    def __div__(self,r):
        return Point(self.x/r,self.y/r)
    def __rmul__(self,r):
        return self.__mul__(r)
    def __str__(self):
        return "<Point(%s,%s)>"%(str(self.x),str(self.y))
