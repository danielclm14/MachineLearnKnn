# -*- coding: utf-8 -*-
from sympy import *
from mpmath import *
import math
import operator 
import pandas
import csv
from numpy import array
import random
class KNN:
    def __init__(self, teste, traine):
        {
	    self.test = teste
        self.train = traine
        }
    
    def euclideanDistance(instance1, instance2, length):
	    distance = 0
	    for x in range(length):
		    distance += pow((instance1[x] - instance2[x]), 2)
	    return math.sqrt(distance)

    
    def getNeighbors(trainingSet, testInstance, k):
	    distances = []
	    length = len(testInstance)-1
	    for x in range(len(trainingSet)):
		    dist = euclideanDistance(testInstance, trainingSet[x], length)
		    distances.append((trainingSet[x], dist))
	    distances.sort(key=operator.itemgetter(1))
	    neighbors = []
	    for x in range(k):
		    neighbors.append(distances[x][0])
	    return neighbors

    def getResponse(neighbors):
        classVotes = {}
        for x in range(len(neighbors)):
                response = neighbors[x][21]
                if response in classVotes:
                    classVotes[response] += 1
                else:
                    classVotes[response] = 1
        sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]

    def getAccuracy(testSet, predictions):
        correct = 0
        for x in range(len(testSet)):
            if testSet[x][21] is predictions[x]:
                correct += 1
        return (correct/float(len(testSet))) * 100.0

    

    def method(self):
        fileOut2 = open('output/euler.csv','a')
        predictions=[]
        k = 10
        for x in range(len(self.test)):
            neighbors = getNeighbors(self.train, self.test[x], k)
            result = getResponse(neighbors)
            predictions.append(result)
            print('> predicted=' + repr(result) + ', actual=' + repr(self.test[x][21]))
        accuracy = getAccuracy(self.test, predictions)
        print('Accuracy: ' + repr(accuracy) + '%')