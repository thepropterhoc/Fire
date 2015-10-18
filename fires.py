

from sklearn import svm
import csv
import numpy as np
from sklearn import cross_validation
import math
import random

print "\nBeginning prediction\n"

def classForContinuous(val):
	parsed = (10 ** val) - 1
	if parsed < 0.1:
		return 0
	elif parsed < 4:
		return 1
	elif parsed < 32:
		return 2
	elif parsed < 80:
		return 3
	elif parsed < 400:
		return 4
	else:
		return 5

inputs,outputs = [], []

days = {
	'mon' : 1,
	'tue' : 2,
	'wed' : 3,
	'thu' : 4,
	'fri' : 5,
	'sat' : 6,
	'sun' : 7
}

months = {
	'jan' : 1,
	'feb' : 2,
	'mar' : 3,
	'apr' : 4,
	'may' : 5,
	'jun' : 6,
	'jul' : 7,
	'aug' : 8,
	'sep' : 9,
	'oct' : 10,
	'nov' : 11,
	'dec' : 12
}

theRows = []

with open('./forestfires.csv', 'r') as csvfile:
	fireReader = csv.reader(csvfile)
	fireReader.next()
	for row in fireReader:
		theRows += [row]

random.shuffle(theRows)

for row in theRows:
	monthFlags = [0] * 12
	monthFlags[months[row[2]] - 1] = 1
	dayFlags = [0] * 7
	dayFlags[days[row[3]] - 1] = 1
	theInput = row[:2] + monthFlags + dayFlags + row[4:-1]
	#theInput = row[-5:-1]
	inputs += [map(float, theInput)]
	outputs += [math.log(float(row[-1]) + 1)]

X_train, X_test, y_train, y_test = cross_validation.train_test_split(inputs, outputs, test_size=0.1, random_state=0)

clf = svm.SVR(kernel='rbf', degree=3, gamma=0.0, coef0=0.0, tol=0.001, C=1.0, epsilon=0.00001, shrinking=True, cache_size=200, verbose=False, max_iter=-1).fit(X_train, y_train)

correct, incorrect, falseNegatives, falsePositives, barelyMissed, severelyMissed, total = 0,0,0,0,0,0,0

for x, y in zip(X_train, map(classForContinuous, y_train)):
	prediction = classForContinuous(clf.predict(x)[0])
	if y == prediction:
		correct += 1
	else:
		incorrect += 1
		if y > 0 and prediction == 0:
			falseNegatives += 1
		elif y == 0 and prediction > 0:
			falsePositives += 1
		elif int(math.fabs(y - prediction)) < 2:
			barelyMissed += 1
		else:
			severelyMissed += 1
	total += 1

print '{0} Correct predictions\n{5} Incorrect predictions\n{1} False Positives (Predicted fire but actually not)\n{2} False Negatives (Predicted no fire, actually was)\n{3} Near misses (Off by 1 class)\n{4} Severe misses (off by more than 1 class)'.format(correct, falsePositives, falseNegatives, barelyMissed, severelyMissed, incorrect)
	



#This code was created and edited by Shelby Vanhooser