import numpy as np
import collections
X = []
y = []
a = []
import csv
f = open('IRIS.csv')
csv_f = csv.reader(f)
for Row in csv_f:
    a.append(Row[4])
    if(Row[0] != "sepal.length"):
        X.append([float(Row[0]),float(Row[1]),float(Row[2]),float(Row[3])])
    if (Row[4] == "Setosa"):
        y.append((1,0,0))
    elif (Row[4] == "Versicolor"):
        y.append((0,1,0))
    else:
        y.append((0,0,1))
f.close()

class NeuralNetwork(object):
    def __init__(self):
        self.lrate = 0.23
        self.inputsize = 4
        self.outputsize = 3
        self.hiddensize = [0] * 2
        self.hiddensize[0] = 6
        self.hiddensize[1] = 4
        self.W1 = np.random.randn(self.inputsize, self.hiddensize[0])
        self.W2 = np.random.randn(self.hiddensize[0], self.hiddensize[1])
        self.W3 = np.random.randn(self.hiddensize[1], self.outputsize)

    def feedForward(self,X):
        self.z = np.dot(X,self.W1)
        self.z1 = self.sigmoid(self.z)
        self.z2 = np.dot(self.z1,self.W2)
        self.z3 = self.sigmoid(self.z2)
        self.z4 = np.dot(self.z3,self.W3)
        output = self.sigmoid(self.z4)
        return output

    def sigmoid(self, s, deriv=False):
        if (deriv == True):
            return s * (1 - s) * self.lrate
        return 1/(1 + np.exp(-s))

    def backward(self,X,y,output):
        self.output_error = y - output
        self.output_delta = self.output_error * self.sigmoid(output, deriv=True)
        self.z3_error = self.output_delta.dot(self.W3.T)
        self.z3_delta = self.z3_error * self.sigmoid(self.z3, deriv=True)
        self.z1_error = self.z3_delta.dot(self.W2.T)
        self.z1_delta = self.z1_error * self.sigmoid(self.z1, deriv=True)
        self.W1 += np.dot(np.transpose(X),self.z1_delta)
        self.W2 += np.dot(self.z1.T,self.z3_delta)
        self.W3 += np.dot(self.z3.T,self.output_delta)

    def train(self, X, y):
        output = self.feedForward(X)
        self.backward(X, y, output)

NN = NeuralNetwork()
for i in range(1000):
    if (i % 100 == 0):
        print("Loss: " + str(np.mean(np.square(y - NN.feedForward(X)))))
    NN.train(X, y)

Z = NN.feedForward(X)
for i in range(0,len(X)):
    Z[i] = Z[i]/np.amax(Z[i])
for item in Z:
    c =int(len(item))
    for temp in range(c):
        if(item[temp]!= 1.0):
            item[temp] = 0
        else:
            item[temp]= 1
l=[]
for i in range(len(Z)):
    if(int(Z[i][0]) == 1):
        l.append("Setosa")
    if(int(Z[i][1]) == 1):
        l.append("Versicolor")
    if(int(Z[i][2]) == 1):
        l.append("Virginica")
for i in range(len(Z)):
    if(l[i] == a[i]):
        c = c+1
print("expected output:\tpredicted output:" )
for i in range(len(Z)):
    print(str(a[i])+ "\t\t\t\t\t\t\t" + str(l[i]) + "\n")
print("Accuracy " + str((c/len(Z))*100))
