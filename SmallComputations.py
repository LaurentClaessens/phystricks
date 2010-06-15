# -*- coding: utf8 -*-

###########################################################################
#	This is part of the module phystricks
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

# copyright (c) Laurent Claessens, 2010
# email: moky.math@gmai.com

"""
This submodule contains functions that perform small computations for phystricks. 
The return values of the functions here are instances of classical classes, not from phystricks classes.
"""

import math
from sage.all import *



# Cette définition retourne l'entier plus grand ou égal à un nombre donné
def CalculEntierPlus(x):
	t = x
	if t <> int(t):
		if t < 0 : t = t-1
		t = int(t) + 1
		return float(t)
	else : return x

# Cette définition retourne l'entier plus grand ou égal à un nombre donné
def CalculEntierMoins(x):
	t = x
	if t <> int(t):
		if t < 0 : t = t-1
		t = int(t)
		return float(t)
	else : return x


def MultipleLower(x,m):
	""" return the biggest multiple of m which is lower or equal to x"""
	return floor(x/m)*m

def MultipleBigger(x,m):
	""" return the lower multiple of m which is bigger or equal to x"""
	return ceil(x/m)*m

def enlarge_a_little_up(x,m,epsilon):
	"""
	see the description of the function enlarge_a_little of the class BoundingBox.
	This function makes the job for one number.
	"""
	if int(x/m) == x/m:
		return x+epsilon
	else : 
		return MultipleBigger(x,m)+epsilon
		
def enlarge_a_little_low(x,m,epsilon):
	"""
	see the description of the function enlarge_a_little of the class BoundingBox.
	This function makes the job for one number.
	"""
	if int(x/m) == x/m:
		return x-epsilon
	else : 
		print "76",x,m,epsilon
		print "77",MultipleLower(x,m)
		return MultipleLower(x,m)-epsilon


def PolarPoint(r,theta):
	return Point(r*math.cos(radian(theta)),r*math.sin(radian(theta)))

class coordinatesPolaires(object):
	def __init__(self,r,theta):
		self.r = r
		self.theta = theta

def PointToPolaire(P):
	"""
	Return the polar coordinates of a point.

	The polar coordinates are given in radian
	"""
	r = P.norme()
	if P.x == 0:
		if P.y > 0:
			alpha = math.pi/2
		if P.y < 0:
			alpha = -math.pi/2
		if P.y == 0 : 			# Convention : l'angle pour le point (0,0) est 0.
			alpha = 0
	else :
		alpha = math.atan(P.y/P.x)
	if (P.x < 0) and (P.y == 0) :
		alpha = math.pi
	if (P.x < 0) and (P.y > 0) :
		alpha = alpha + math.pi
	if (P.x < 0) and (P.y < 0 ) :
		alpha = alpha +math.pi
	#theta = degree(alpha)
	return coordinatesPolaires(r,alpha)

def radian(theta):
	return theta*math.pi/180
def degree(alpha):
	return 180*alpha/math.pi

def Distance_sq(P,Q):
	""" return the squared distance between P and Q """
	return (P.x-Q.x)**2+(P.y-Q.y)**2

def Distance(P,Q):
	""" return the distance between P and Q """
	return math.sqrt(Distance_sq(P,Q))
