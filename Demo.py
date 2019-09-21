from Matrex import Matrex, makeLaetx2dGeneric
import numpy as np

print("MATREX DEMO")
print("---------------------------")
print("life hack: there's 2 ways to get people to code a library for you.  1) pay them. 2)spend 15 minutes starting it then ask them to finish it")
print("--------------------------")

print("\n====generic dxn matrix.====\n")
tex = makeLaetx2dGeneric(filename = "tex/hw.tex", atLine = 23)
print(tex)
print("\n====from nested lists.====\n")
m = Matrex([[3,4,5],[5,6,7],[8,9,10]])
tex = m.makeLatex(filename = "tex/hw2.tex", atLine = 23)
print(tex)
print("\n====from an np array.====\n")
arr = np.asarray([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]])
m = Matrex(arr)
tex = m.makeLatex(filename = "tex/hw3.tex", atLine = 23)
print(tex)
print("\n====from np zeros.====\n")
m = Matrex(3,4,dtype=str)
tex = m.makeLatex(filename = "tex/hw4.tex", atLine = 23)
print(tex)