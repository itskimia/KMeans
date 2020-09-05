# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:13:10 2020

@author: hashemi
"""

import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



    

def dist (x1, y1, x2, y2):
    
    d = np.sqrt((x1-x2)**2 + (y1-y2)**2)
    return d


def findCluster (data, centroids, k, ii, colmap):
    kk=0
    mini = 1000
               
    for i in centroids.keys():
        temp = dist(data.at[ii,'X'], data.at[ii, 'Y'], centroids[i][0], centroids[i][1])

        if temp < mini:
            mini = temp
            kk = i

    data.at[ii, 'coloor'] = colmap[kk]
    
    
def updateCentroids (data, centroids, colmap):
    for i in centroids.keys():
        for j in range(size):
            centroids[i][0] = np.mean(data[data['coloor'] == colmap[i]]['X'])
            centroids[i][1] = np.mean(data[data['coloor'] == colmap[i]]['Y'])
    
    return centroids




def calError (data, centroids, colmap):
    err=dict()
    for i in centroids.keys():
        for j in range(size):
            err[i] += err[i] + dist(data[data['coloor'] == colmap[i]]['X'], data[data['coloor'] == colmap[i]]['Y']
                 ,centroids[i][0], centroids[i][1])**2
    
    return err



def kmeans(data, k, n):
    
    arr = random.sample(range(1, size), k)
    
    centroids = {
        i+1: [data.at[arr[i],'X'], data.at[arr[i],'Y']]
        for i in range(k)
    }
    
    
    colmap = {
        i+1: i+1
        for i in range(k)
    }
    
    j=[]
    for l in range(size):
        j.append('b')
        
    data = data.assign(coloor= j)
    
    for i in range(size):
        findCluster(data, centroids, k, i, colmap)
        
    
    plt.scatter(data['X'], data['Y'], c=data['coloor'], alpha=0.5, edgecolor='k')
    plt.show()

    for i in range(n):
        NewCentroids = updateCentroids(data, centroids, colmap)
        for i in range(size):
            findCluster(data, NewCentroids, k, i, colmap)

        plt.scatter(data['X'], data['Y'], c=data['coloor'], alpha=0.5, edgecolor='k')
        plt.show()

    #Errors of each cluster for an specific k
    error = {
        i+1: 0
        for i in range(k)
    }
    
    
    for i in centroids.keys():
        err2 =  dist(data[data['coloor'] == colmap[i]]['X'], data[data['coloor'] == colmap[i]]['Y'],centroids[i][0], centroids[i][1])**2
        error[i]= np.sum(err2) / len(err2)
    
    print("Cluster errors:")
    for i in centroids.keys():
        print("k:" + str(i) + "    " + str(error[i]))


    #Average clustering error for an specific k
    sumofE = 0
    for i in centroids.keys():
        sumofE += error[i]
        
    avgErr = sumofE/k
    
    return avgErr
    

if __name__ == "__main__":

    #change dataset for part E
    data = pd.read_csv("Dataset1.csv")
    
    size = data["X"].size
    k = 4
    n = 15

    plt.scatter(data["X"], data["Y"], color='')
    
    
    
    
    #Parts: A-B-C-F
    #Printing the average clustering error as the result of the K-means function
    print("Average Clustering Error:  " + str(kmeans(data, k, n)))
    
    


    #Part: D
    
    listofp=[]
    for k in range(2,15):
         A = kmeans(data ,k, 3)
         listofp.append(A)
    plt.plot(listofp)
    plt.show()
    
    
    
    
    