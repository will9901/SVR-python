# -*- coding: utf-8 -*-
# 作者         ：HuangJianyi
import MySQLdb
import numpy as np
from sklearn import linear_model
from sklearn.tree import tree
from sklearn.gaussian_process import GaussianProcess
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
import math

def bayesianARDregression(x_list_train,y_list_train,x_list_test):
	clf = linear_model.ARDRegression()
	clf.fit (x_list_train,y_list_train)
	print("Bayesian ARD Regression:")
	print(clf.coef_)
	y_predict_list = clf.predict(x_list_test)
	print(y_predict_list)
	return y_predict_list

def main():
	file2 = open("./eventtimefactor2.txt",'r')
	i = 1
	x_list_test = list()
	y_list_test = list()
	x_list_train = list()
	y_list_train = list()
	for line in file2:
		line = line.strip('\n')
		line_splitted = line.split('\t')
		y = int(line_splitted[1])
		x_1 = float(line_splitted[7])
		x_2 = float(line_splitted[11])
		x_3 = float(line_splitted[13])
		# print x_1+'\t'+x_2+'\t'+x_3+'\t'+y
		x_single_list = [x_1,x_2,x_3]
		if i <= 87:
			y_list_test.append(y)
			x_list_test.append(x_single_list)
		else:
			y_list_train.append(y)
			x_list_train.append(x_single_list)
		i += 1
	file2.close()

	y_predict_list_4 = bayesianARDregression(x_list_train,y_list_train,x_list_test)

	file1=open("./bursttime_predict_result_bayes.txt",'w')
	sum_4 = 0

	line_list = list()
	y_predict_real_list_4 = list()
	# single_line = 'real'+'\t'+'SVR'
	# line_list.append(single_line)
	for i in range(0,len(x_list_test)):
		if y_predict_list_4[i] < 0:
			y_predict_list_4[i] = 1
		y_predict_list_int_4 = int(round(y_predict_list_4[i]))

		y_predict_real_4 = y_predict_list_int_4

		y_predict_real_list_4.append(y_predict_real_4)

		sum_4 += float(abs(y_predict_real_4 - int(y_list_test[i])))/int(y_list_test[i])

		single_line = str(y_list_test[i]) +'\t'+ str(y_predict_real_4)
		line_list.append(single_line)

	mape4 = sum_4/len(x_list_test)


	# single_line = '0' +'\t'+ str(mape4)
	# line_list.append(single_line)
	write_content = '\n'.join(line_list)
	file1.write(write_content)
	file1.close()

if __name__ == "__main__":
	main()