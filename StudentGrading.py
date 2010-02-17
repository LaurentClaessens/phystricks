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
This module uses phystricks in order to produces graphics of the grading. 

From a list of number, we can generate 3 graphics
1. y = percent of students which obtained more or equal to x
(to be implemented):
2. y = average points of the students who obtained more or equal to x
1. y = number of students who obtained x plus or minus 1.

"""

from __future__ import division
import commands, os, copy, math						# La classe copy est pour faire des copies d'objets
from sage.all import *
from phystricks import *

REP = commands.getoutput("pwd")

class Grades(object):
	"""
	list : 	The list of grades that are given.
	max : the maximal note
	"""
	def __init__(self,list,max):
		self.list = list
		self.max = max
	def list_with_max(self,n):
		""" return the list of grades if the maximum is n instead of self.max """
		return [ c*n/self.max for c in self.list ]
	def y_is_percent_bigger_than_x(self,name,max):
		"""
		Generates the figure that represent the graph of the function
		x -> y = percent of the students that have x or more.
		The intervals are x=[0,n] and y=[0,1]

		n is the maximum grade
		name is the name of the files to be created
		"""
		pspict=pspicture(name)
		fig = GenericFigure(name)

		cloud = []
		for x in range(0,max+1):
			y = PercentHaveMore(self.list_with_max(max),x)
			p = Point( x, y )
			P = Graph(p)
			P.parameters.color = "blue"
			pspict.DrawGraph(P)

		segment = Segment( Point(0,50),Point(max,50) )
		S = Graph(segment)
		S.parameters.color = "red"
		pspict.DrawGraph( S )

		pspict.grid.Dy = 10
		pspict.grid.num_subX = 0
		pspict.grid.num_subY = 5
		pspict.axes.Dy = 10
		pspict.DrawDefaultAxes()
		pspict.DrawDefaultGrid()

		pspict.dilatation_Y(0.1)

		fig.add_pspicture(pspict)
		fig.conclude()
		fig.write_the_file()

def PercentHaveMore(cotes,n):
	return ProportionHaveMore(cotes,n)*100

def ProportionHaveMore(cotes,n):
	"""
	Returns the proportion of elements in cotes that are bigger than n
	"""
	return HaveMore(cotes,n)/len(cotes)

def HaveMore(cotes,n):
	"""
	returns the number of elements of the list cotes that are bigger than n
	"""
	a = 0
	for p in cotes:
		if p >= n : a=a+1
	return a	

def CombienAutour(cotes,n,delta):
	a = 0
	for p in cotes:
		if abs(p-n)<=delta : a=a+1
	return a	

def CombienMoyAuDessus(cotes,n):
	a = 0
	s = 0
	for p in cotes:
		if p > n : 
			a=a+1
			s=s+p
	if a == 0 : return 0
	if a <> 0 : return s/a

def GrapheNuage(nuage,prefixe,suffixe):
	pspict=pspicture()
	fig = GenereFigure(REP,prefixe+suffixe)

	pspict.BB.AddPoint(Point(0,0))				
	pspict.TraceNuage_de_Points(nuage,"*","")

	pspict.grille.AjouteOption("linecolor=lightgray")
	if pspict.BB.tailleY() > 10 :
		pspict.axes.AjouteOption("Dy=2")
	pspict.TraceGrilleDefaut()
	pspict.TraceAxesDefaut()

	pspict.fixe_tailleX(15)
	pspict.fixe_tailleY(5)

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()

def CreeGraphiques(audit,exam):
	cotes_pures = audit.liste_cotes(exam)
	cotes = cotes_pures
	suffixe = audit.section+exam.nom+"A"

	nuage = Nuage_de_Points()
	for n in range(1,20):
		nuage.ajoute_point(Point(n,CombienPlus(cotes,n)))
	GrapheNuage(nuage,"CombienPlus",suffixe)


	nuage = Nuage_de_Points()
	for n in range(1,20):
		nuage.ajoute_point(Point(n, CombienMoyAuDessus(cotes,n)))
	GrapheNuage(nuage,"MoyenneAuDessus",suffixe)

	nuage = Nuage_de_Points()
	for n in range(2,20):
		nuage.ajoute_point(Point(n, CombienAutour(cotes,n,1)))
	GrapheNuage(nuage,"CombienAutour",suffixe)


def ListeToGraphiques(liste,nomAudit,nomMatiere,nomExam) :
	n = len(liste)
	auditoire = Auditoire(nomAudit,nomMatiere)
	listeEtudiants = []
	for i in range(0,len(liste)) :
		listeEtudiants.append(Etudiant("P"+str(i),"N"+str(i)))
	for i in range(0,len(liste)) :
		auditoire.ajoute_etudiant(listeEtudiants[i])
		listeEtudiants[i].ajoute_cote(nomExam,liste[i])
	for et in auditoire.liste_etudiants :
		print et.nom+" "+et.prenom+" "+str(et.dico_cotes[nomExam])
	
	CreeGraphiques(auditoire,nomExam)	


