"""
Author : Jarly Arciniega
Assignment 12
Program : Polynomials
Program Description: write a class that adds, subtracts and multiplies and divisions is xtra points

"""


# this imports the regex module which helps with the find all that used in the string while parsing it since this needs
# to be done in carrot form (4x^4) or so
import re


class Polynomial(object):
    def __init__(self, val):
        if type(val) == type([]):
            self.plist = val
        elif type(val) == type(''):
            self.plist = parse_string(val)
        else:
            raise "Unknown argument to Polynomial: %s" % val
        return

    def __add__(self,other):
        return Polynomial(add(self.plist,plist(other)))

    def __sub__(self,other):
        return Polynomial(sub(self.plist,plist(other)))

    def __mul__(self,other):
        return Polynomial(multiply(self.plist, plist(other)))

    def __pow__(self,e):
        return Polynomial(power(self.plist,e))

    def __repr__(self):
        return tostring(self.plist)


def plist(term):
    '''Force term to have the form of a polynomial list'''
    # First see if this is already a Polynomial object
    try:
        pl = term.plist
        return pl
    except:
        pass

    # It isn't. Try to force coercion from an integer or a float
    if type(term) == type(1.0) or type(term) == type(1):
        return [term]
    elif type(term) == type(''):
        return parse_string(term)
    
    else:
        raise "Unsupported term can't be corced into a plist: %s" % term
    return None


def add(p1, p2):
    "Return a new plist corresponding to the sum of the two input plists."
    if len(p1) > len(p2):
        new = [i for i in p1]
        for i in range(len(p2)): new[i] += p2[i]
    else:
        new = [i for i in p2]
        for i in range(len(p1)): new[i] += p1[i]
    return new

def sub(p1,p2):
    return add(p1, mult_const(p2, -1))

def mult_const(p,c):
    "Return a new plist corresponding to the input plist multplied by a const"
    return [c*pi for pi in p]

def multiply(p1,p2):
    "Return a new plist corresponding to the product of the two input plists"
    if len(p1) > len(p2):
        short, long = p2,p1
    else:
        short,long = p1,p2
    new = []
    for i in range(len(short)):
        new = add(new,mult_one(long,short[i],i))
    return new

def mult_one(p,c,i):
    """\
    Return a new plist corresponding to the product of the input plist p
    with the single term c*x^i
    """
    new = [0]*i # increment the list with i zeros
    for pi in p: new.append(pi*c)
    return new

def power(p,e):
    "Return a new plist corresponding to the e-th power of the input plist p"
    assert int(e) == e
    new = [1]
    for i in range(e): new = multiply(new,p)
    return new

def parse_string(str=None):
    termpat = re.compile('([-+]?\s*\d*\.?\d*)(x?\^?\d?)')
    res_dict = {}
    for n,p in termpat.findall(str):
        n,p = n.strip(),p.strip()
        if not n and not p: continue
        n,p = parse_n(n),parse_p(p)
        if res_dict.has_key(p): res_dict[p] += n
        else: res_dict[p] = n
    highest_order = max(res_dict.keys())
    res = [0]*(highest_order+1)
    for key,value in res_dict.items(): res[key] = value
    return res

def parse_n(str):
    "Parse the number part of a polynomial string term"
    if not str: return 1
    elif str == '-': return -1
    elif str == '+': return 1
    return eval(str)

def parse_p(str):
    "Parse the power part of a polynomial string term"
    pat = re.compile('x\^?(\d)?')
    if not str:
        return 0
    res = pat.findall(str)[0]
    if not res:
        return 1
    return int(res)

def strip_leading_zeros(p):
    "Remove the leading (in terms of high orders of x) zeros in the polynomial"
    # compute the highest nonzero element of the list
    for i in range(len(p)-1,-1,-1):
        if p[i]:
            break
    return p[:i+1]

def tostring(p):
    """\
    Convert a plist into a string.
    """
    p = strip_leading_zeros(p)
    str = []
    for i in range(len(p)-1,-1,-1):
        if p[i]:
            if i < len(p)-1:
                if p[i] >= 0: str.append('+')
                else: str.append('-')
                str.append(tostring_term(abs(p[i]),i))
            else:
                str.append(tostring_term(p[i],i))
    return ' '.join(str)

def tostring_term(c,i):
    "Convert a single coefficient c and power e to a string cx^i"
    if i == 1:
        if c == 1: return 'x'
        elif c == -1: return '-x'
        return "%sx" % c
    elif i:
        if c == 1: return "x^%d" % i
        elif c == -1: return "-x^%d" % i
        return "%sx^%d" % (c,i)
    return "%s" % c

def test():

    A = (Polynomial('3x - 4x^2 + 7x^5-x+1'))
    B = (Polynomial('4x + 7x^5-x+2'))
    A2 = (Polynomial('5x+x^2'))
    C = A.__sub__(B)
    D = A.__add__(7)
    E = A2.__mul__(A2)
    print(C)
    print(D)
    print(E)


test()

'''''
C:\Python27\python.exe C:/Users/Jarly/PycharmProjects/untitled/ProjectsPython/testing.py
-4x^2 - x - 1
7x^5 - 4x^2 + 2x + 8
x^4 + 10x^3 + 25x^2

Process finished with exit code 0
'''''