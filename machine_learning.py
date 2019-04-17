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

def svmRegression(x_list_train,y_list_train,x_list_test):
	clf = svm.SVR(C=1000,gamma=0.0001)
	clf.fit(x_list_train,y_list_train)
	print("SVR:")
	y_predict_list = clf.predict(x_list_test)
	print(y_predict_list)
	return y_predict_list

def main():
	file2 = open("./eventtimefactor10.txt",'r')
	i = 1
	x_list_test = list()
	y_list_test = list()
	x_list_train = list()
	y_list_train = list()
	for line in file2:
		line = line.strip('\n')
		line_splitted = line.split('\t')
		y = line_splitted[1]
		#x_1 = line_splitted[4]
		#x_2 = line_splitted[5]
		#x_3 = line_splitted[6]
		x_4 = line_splitted[7]
		#x_5 = line_splitted[8]
		#x_6 = line_splitted[9]
		#x_7 = line_splitted[10]
		#x_8 = line_splitted[11]
		x_9 = line_splitted[12]
		#x_10 = line_splitted[13]
		#x_11 = line_splitted[14]
		#x_12 = line_splitted[15]
		#x_13 = line_splitted[16]
		# print x_1+'\t'+x_2+'\t'+x_3+'\t'+y
		x_single_list = [x_4,x_9]
		if 87*4<i <= 87*5:
			y_list_test.append(y)
			x_list_test.append(x_single_list)
		else:
			y_list_train.append(y)
			x_list_train.append(x_single_list)
		i += 1

	y_predict_list_4 = svmRegression(x_list_train,y_list_train,x_list_test)

	file1=open("./bursttime_predict_result_C1000_gamma00001_mape.txt",'w')
	sum_4 = 0

	line_list = list()
	y_predict_real_list_4 = list()
	single_line = 'real'+'\t'+'SVR'
	line_list.append(single_line)
	for i in range(0,len(x_list_test)):
		if y_predict_list_4[i] < 0:
			y_predict_list_4[i] = 1
		y_predict_list_int_4 = int(round(y_predict_list_4[i]))

		y_predict_real_4 = y_predict_list_int_4

		y_predict_real_list_4.append(y_predict_real_4)

		# sum_4 += float(abs(y_predict_real_4 - int(y_list_test[i])))/int(y_list_test[i])
		sum_4 += (y_predict_real_4 - int(y_list_test[i]))**2

		single_line = str(y_list_test[i]) +'\t'+ str(y_predict_real_4)
		line_list.append(single_line)

	mape4 = sum_4/len(x_list_test)
	rmse4 = mape4 ** 0.5

	single_line = '0' +'\t'+ str(rmse4)
	line_list.append(single_line)
	write_content = '\n'.join(line_list)
	file1.write(write_content)
	file1.close()

if __name__ == "__main__":
	main()