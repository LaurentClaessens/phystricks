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

"""
This file contains the utilities that do not depend on sage or other
parts of phystricks.

So you can safely import from here.
"""

def text_to_hexdigest(text):
    """
    Return the sha1 hexdigest of a text.

    The point of this function is to take care about the fact
    that the hashlib wants 'str', not 'unicode'
    """
    import hashlib
    str_text=ensure_str(text)

    h=hashlib.new("sha1")
    h.update(str_text)            # This one wants 'str', not 'unicode'
    return h.hexdigest()

def first_bracket(text):
    """
    return the first bracket in the string 'text'  
    """
    if "[" not in text:
        return ""
    a=text.find("[")
    b=text[a:].find("]")+1+a
    bracket=text[a:b]
    return bracket


def ensure_unicode(s):
    """
    Return a 'unicode' object that represents 's'. 
    No conversion if 's' is already unicode.

    str->unicode (via s.decode("utf8"))
    unicode->unicide (identity map)
    """
    if isinstance(s,str):
        return s.decode("utf8")
    if isinstance(s,unicode):
        return s
    testtype(s)
    raise TypeError("You are trying to convert to unicode the following object "+str(s)+" of type "+str(type(s)))

def ensure_str(s):
    """
    Return a 'str' object that represents 's'. 
    No conversion if 's' is already str.

    unicode->str (via s.encode("utf8"))
    str->str (identity map)
    """
    if isinstance(s,str):
        return s
    if isinstance(s,unicode):
        return s.encode("utf8")
    else :
        rep=str(s)
        return ensure_str(rep)
    testtype(s)
    raise TypeError("You are trying to convert to unicode the following object "+str(s)+" of type "+str(type(s)))

def logging(text,pspict=None):
    from Defaults import LOGGING_FILENAME
    import codecs
    text=ensure_unicode(text)
    if pspict :
        text="in "+pspict.name+" : "+text
    print(text)
    with codecs.open(LOGGING_FILENAME,"a",encoding="utf8") as f:
        f.write(text+"\n")

class SubdirectoryFilenames(object):
    """
    An object of this class represent a file, 
    or more precisely the path to a file.

    If the file "Directories.py" exists, read the directories in which the 
    tex files have to be put.
    In all cases if the file "Directories.py" is not found, everything will
    return the unmodified filename.
    """
    def __init__(self,filename,position="here"):
        """
    - `filename` is a string containing the filenam
        e with no directory indications.
    - `position` can be "here", "main" or "tex" (default "here")

        if "here" : the file is in the current directory
                when the picture is created.
                    That is the current directory with respect to Sage
        if "main" : the file is in the main latex directory
        if "tex" : the file is un the picture latex directory, that is the
                    directory in which the file ".pstricks" is put.
        if "tikz" : the file is the directiry for md5 and pdf tikz files.
        """
        import os.path
        self.filename=filename
        self.position=position
        if os.path.isfile("Directories.py"):

            # 'importlib' is the solution for python3
            # 'imp' is the solution for python2
            # This class is imported by python3 from the script 
            # 'new_picture.py'
            try :
                import importlib.util
                spec = importlib.util.spec_from_file_location("Directories", "Directories.py")
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
            except ImportError :
                import imp
                module = imp.load_source("Directories","Directories.py")


            self.PICTURES_TEX=module.PICTURES_TEX
            self.PICTURES_SRC=module.PICTURES_SRC
            self.PICTURES_TIKZ=module.PICTURES_TIKZ
            self.MAIN_TEX=module.MAIN_TEX

            if position=="here":
                self.abs_filename=os.path.abspath(filename)
            if position=="main":
                ff=os.path.join(self.MAIN_TEX,filename)
                self.abs_filename=os.path.abspath(ff)
            if position=="pictures_tex":
                ff=os.path.join(self.PICTURES_TEX,filename)
                self.abs_filename=os.path.abspath(ff)
            if position=="pictures_src":
                ff=os.path.join(self.PICTURES_SRC,filename)
                self.abs_filename=os.path.abspath(ff)
            if position=="pictures_tikz":
                ff=os.path.join(self.PICTURES_TIKZ,filename)
                self.abs_filename=os.path.abspath(ff)
        else :
            self.abs_filename=os.path.abspath(filename)
    def from_here(self):
        import os.path
        if not os.path.isfile("Directories.py"):
            return self.filename
        current="."
        tex=os.path.relpath(self.PICTURES_TEX,current)
        ff=os.path.relpath(self.abs_filename,current)
        return ff
    def from_main(self):
        import os.path
        if not os.path.isfile("Directories.py"):
            return self.filename
        current="."

        main=os.path.relpath(self.MAIN_TEX,current)
        tex=os.path.relpath(self.PICTURES_TEX,current)
        vfile=self.abs_filename

        ff=os.path.relpath(self.abs_filename,main)
        return os.path.relpath(vfile,main)
    def abspath(self):
        return self.abs_filename

def unify_point_name(s):
    r"""
    Interpret `s` as the pstricks code of something and return a chain with
    all the points names changed to "Xaaaa", "Xaaab" etc.

    Practically, it changes the strings like "{abcd}" to "{Xaaaa}".

    When "{abcd}" is found, it also replace the occurences of "(abcd)".
    This is because the marks of points are given by example as
    '\\rput(abcd){\\rput(0;0){$-2$}}'

    This serves to build more robust doctests by providing strings in which
    we are sure that the names of the points are the first in the list.

    INPUT:

    - ``s`` - a string

    OUTPUT:
    string

    EXAMPLES:
    
    In the following example, the points name in the segment do not begin
    by "aaaa" because of the definition of P, or even because of other doctests executed before.
    (due to complex implementation, the names of the points are
    more or less unpredictable and can change)

    ::

        sage: from phystricks import *
        sage: P=Point(3,4)
        sage: S = Segment(Point(1,1),Point(2,2))

    However, using the function unify_point_name, the returned string begins with "Xaaaa" ::

    Notice that the presence of "X" is necessary in order to avoid
    conflicts when one of the points original name is one of the new points name as in the following example ::

        sage: s="{xxxx}{aaaa}{yyyy}"
        sage: print unify_point_name(s)
        {Xaaaa}{Xaaab}{Xaaac}

    Without the additional X,

    1. The first "xxxx" would be changed to "aaaa".
    2. When changing "aaaa" into "aaab", the first one would be changed too.

    """
    raise DeprecationWarning
    import re

    point_pattern=re.compile("({[a-zA-Z]{4,4}})")
    match = point_pattern.findall(s)

    rematch=[]
    for m in match:
        n=m[1:-1]       # I transform "{abcd}" into "abcd"
        if n not in rematch:
            rematch.append(n)

    from phystricks.src.PointGraph import PointsNameList
    names=PointGraph.PointsNameList()
    for m in rematch:
        name=names.next()
        s=s.replace("{%s}"%m,"{X%s}"%name).replace("(%s)"%m,"(X%s)"%name)
    return s
