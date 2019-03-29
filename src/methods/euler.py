# -*- coding: utf-8 -*-
from sympy import *
from mpmath import *
class Euler:
    def __init__(self, info):
		self.inputi = info

    def method(self):
        fileOut = open('output/saida.txt','a')
        fileOut2 = open('output/euler.csv','w')
        t, y = symbols("t y")
        function = sympify(self.inputi[5])
        y0, t0, h, n = sympify(self.inputi[1]), sympify(self.inputi[2]), sympify(self.inputi[3]), sympify(self.inputi[4]) 
        fileOut.write("\nMetodo de " + self.inputi[0] + "\n")
        fileOut.write("y(" + str(t0) + ") = " + str(y0) + "\n")
        fileOut.write("H = " + str(h) + "\n")

        for j in range(0, n+1):
            k1 = function.subs([(t, t0), (y, y0)])
            fileOut.write(str(j))
            fileOut.write(" ")
            fileOut.write(str(y0))
            fileOut.write("\n")
            fileOut2.write(str(j))
            fileOut2.write(" ")
            fileOut2.write(str(y0))
            fileOut2.write("\n")
            y0 = y0 + h*k1
            t0 = t0 + h
        fileOut.close()
        fileOut2.close()




