# -*- coding: utf-8 -*-
from sympy import *
from mpmath import *
import pandas
import math
import operator 
# from methods.knn import KNN
import csv
from numpy import array
import random
from sklearn.model_selection import KFold

def euclideanDistance(instance1, instance2, length):
        distance = 0
        for x in range(length):
                distance += pow((float(instance1[x]) - float(instance2[x])), 2)
                # print(distance)
        return math.sqrt(distance)


def getNeighbors(trainingSet, testInstance, k):
        distances = []
        length = 20
        for x in range(len(trainingSet)-1):
                dist = euclideanDistance(testInstance, trainingSet[x], length)
                distances.append((trainingSet[x], dist))
        distances.sort(key=operator.itemgetter(1))
        neighbors = []
        for x in range(k):
                neighbors.append(distances[x][0])
        return neighbors

def getResponse(neighbors):
        classVotes = {}
        for x in range(len(neighbors)-1):
                response = neighbors[x][21]
                if response in classVotes:
                        classVotes[response] += 1
                else:
                        classVotes[response] = 1
        sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
        correct = 0
        for x in range(len(testSet)-1):
                if (testSet[x][21] == predictions[x]):
                        correct += 1
        return ((correct/float(len(testSet))) * 100.0)



def method(teste, traine, k):
        fileOut = open('output/knn.csv','a')
        predictions=[]
        for x in range(len(teste)-1):
                neighbors = getNeighbors(traine, teste[x], k)
                result = getResponse(neighbors)
                predictions.append(result)
                # print('> predicted= ' + repr(result) + ', actual= ' + repr(teste[x][21]))
        accuracy = getAccuracy(teste, predictions)
        # print('Accuracy: ' + repr(accuracy) + '%')
        # fileOut.write(repr(accuracy))
        fileOut.close()
        return accuracy

def main():
        #fileIn = open('input/input.txt', 'r')
        logsini = []
        fileOut = open('output/knn.csv','w')
        fileOut.close()
        with open('input/kc1nd.csv', 'r') as fileIn:
                # for line in fileIn:
                #     logsini.append(line)
                lines = csv.reader(fileIn)
                for line in lines:
                        # print(line)
                        logsini.append(line)
        fileIn.close()
        
        rst = 0
        data = array(logsini)
        kfold = KFold(10, True, 1)
        for k in range(2, 15):
                for train, test in kfold.split(data):
                        # print('train: %s, test: %s \n' % (data[train], data[test]))
                        # print(len(data))
                        # print(len(data[train][2]))
                        # print(data[test][0][0])
                        for x in range(len(data[test])-1) :
                                for y in range(20):
                                        data[test][x][y] = float(data[test][x][y])
                        for x in range(len(data[train])-1) :
                                for y in range(20):
                                        data[train][x][y] = float(data[train][x][y])
                        
                        rst += method(data[test],data[train],k)
                print(rst/float(10))
                rst = 0


if __name__ == '__main__':
	main()




