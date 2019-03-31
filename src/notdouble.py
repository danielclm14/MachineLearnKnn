# -*- coding: utf-8 -*-
from sympy import *
from mpmath import *
from sklearn.model_selection import KFold
import csv
import random

def main():
    fileOut = open('input/cm1nd.csv','w')
    logsin = []
    with open('input/cm1.csv', 'r') as fileIn:
        for line in fileIn:
            logsin.append(line)
    fileIn.close()
    filenotdouble = set(logsin)
    for line in filenotdouble:
        fileOut.write(line)
    
    fileOut.close()

if __name__ == '__main__':
	main()
