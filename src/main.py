# -*- coding: utf-8 -*-
from sympy import *
from mpmath import *
import pandas
# from methods.euler import Euler
import csv
from numpy import array
import random
from sklearn.model_selection import KFold

def main():
    #fileIn = open('input/input.txt', 'r')
    logsini = []
    
    with open('input/cm1nd.csv', 'r') as fileIn:
        # for line in fileIn:
        #     logsini.append(line)
        lines = csv.reader(fileIn)
        for line in lines:
            print(line) 
            logsini.append(lines)
    fileIn.close()

    data = array(logsini)
    kfold = KFold(10, True, 1)
    # for train, test in kfold.split(data):
        # print('train: %s, test: %s \n' % (data[train], data[test]))
        # print(len(data))
        # print(str(data[train]))
        # print(str(data[test]))

if __name__ == '__main__':
	main()




