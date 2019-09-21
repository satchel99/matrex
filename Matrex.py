import numpy as np

TAB = "\t"
PACKAGE = r'\usepackage{amsmath}'

class Matrex:
    def __init__(self, *args, **kwargs):
        if(len(args) == 0):
            self.data = np.zeros([2, 2], dtype = int) 
        if(len(args) == 1):
            if(isinstance(args[0], np.ndarray)):
                self.data = args[0]
            elif(isinstance(args[0], list)):
                self.data = np.asarray(args[0])
            else:
                raise ValueError("if 1 argument is passed, it must be a numpy array or a list")
        else:
            dimensions = []
            for i in args:
                if(not isinstance(i, int)):
                    raise ValueError("if more than one arg passed, they should represent the dimensions of an nd-matrix")
                else:
                    dimensions.append(i)
            if(kwargs.get("dtype") != None):
                self.data = np.zeros(dimensions, dtype = kwargs.get("dtype"))
            else:
                self.data = np.zeros(dimensions, dtype = int)
    def __str__(self):
        return str(self.data)
    def __repl__(self):
        return str(self.data)
    def __setitem__(self, index, value):
        self.data[index] = value
    def makeLatex(self, filename, atLine = None):
        rs = r"\begin{bmatrix}"
        rs = rs + "\n"
        dimensions = self.data.shape
        for i in range(0, dimensions[0]):
            for j in range(0, dimensions[1]):
                end = " & "
                if(j == dimensions[1] - 1):
                    end = " "
                rs = rs + str(self.data[i][j]) + end
            end = r" \\ "
            if(i == dimensions[0] - 1):
                end = ""
            rs = rs + end + "\n"
        rs = rs + "\end{bmatrix}\n"
        if(filename != None):
            push(rs,filename,atLine=atLine)
        return rs
def readFile(filename):
    try:
        f = open(filename, "r")
        lines = []
        for line in f.readlines():
            lines.append(line)
        f.close()
        return lines
    except:
        return False
def write(filename, lines):
    f = open(filename, "w")
    for line in lines:
        f.write(line)
    f.close()
def push(rs,filename,atLine=None):
    lines = readFile(filename)
    if(lines == False):
        raise ValueError("invalid filename")
    if(atLine == None):
        lines.append(rs)
    else:
        tmp = lines[0:atLine]
        tmp.append(rs)
        tmp.extend(lines[atLine:])
        lines = tmp
    write(filename, lines)
def makeLaetx2dGeneric(filename=None,atLine=None,baseVariable="x"):
    rs = r'''\begin{bmatrix}
    x_{11} & x_{12} & x_{13} & \dots  & x_{1n} \\
    x_{21} & x_{22} & x_{23} & \dots  & x_{2n} \\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    x_{d1} & x_{d2} & x_{d3} & \dots  & x_{dn}
    \end{bmatrix}'''
    rs = rs + "\n"
    if(filename != None):
        push(rs,filename,atLine=atLine)
    return rs