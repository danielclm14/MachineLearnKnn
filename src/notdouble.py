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

    kfold = KFold(10, True, 1)
    for train, test in kfold.split(filenotdouble):
        print('train: %d, test: %d' % (len(filenotdouble[train]), len(filenotdouble[test])))



if __name__ == '__main__':
	main()
