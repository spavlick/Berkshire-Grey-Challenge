import os
from os import listdir
from os.path import isfile, join

def file_search(mypath, regex):
	''' This is a function to find all files in a directory containing a certain regex
	in the filename.
	Inputs:
	mypath: the path to the directory you wish to search
	regex: the expression to find in the files
	Outputs:
	regex_files: all the files found in the given directory matching the given regex
	'''
	try:
		regex_files = [f for f in listdir(mypath) if isfile(join(mypath, f)) and regex in f]
		print("Our code found ", str(len(regex_files)), " files that match your criteria")
		return regex_files
	except FileNotFoundError:
		print('Please enter a valid directory')


def test1():
	'''This test case creates a few filenames in a directory and finds which files match 
	the regex. There are 3 matching and 3 nonmatching files. The regex is at the 
	beginning of the filename.
	'''
	mypath = os.path.join(os.getcwd(), 'test1/')
	if not os.path.isdir(mypath):
		os.mkdir(mypath)
	#create files in directory
	for i in range(3):
		f = open(mypath+str('hello'+str(i)+'.txt'),'w')
		f.close()
		f = open(mypath+str('bye'+str(i)+'.txt'),'w')
		f.close()
	files = file_search(mypath,'hello')
	print(files)

def test2():
	'''This test case tests finding files matching the regex when no
	filenames contain the expression.
	'''
	mypath = os.path.join(os.getcwd(), 'test2/')
	if not os.path.isdir(mypath):
		os.mkdir(mypath)
		#create files in directory
	for i in range(3):
		f = open(mypath+str('goodbye'+str(i)+'.txt'),'w')
		f.close()
		f = open(mypath+str('bye'+str(i)+'.txt'),'w')
		f.close()
	files = file_search(mypath,'hello')
	print(files)

def test3():
	'''This test case tests throwing an exception when the directory is 
	invalid.
	'''
	mypath = ''
	files = file_search(mypath,'hello')
	print(files)

def test4():
	'''This test case tests finding files matching the regex when the 
	regex is not at the beginning of the filenames.
	'''
	mypath = os.path.join(os.getcwd(), 'test4/')
	if not os.path.isdir(mypath):
		os.mkdir(mypath)
		#create files in directory
	for i in range(3):
		f = open(mypath+str(str(i)+'hello'+'.txt'),'w')
		f.close()
		f = open(mypath+str(str(i)+'bye'+'.txt'),'w')
		f.close()
	files = file_search(mypath,'hello')
	print(files)

def test5():
	'''This test case tests finding files matching the regex when there 
	are many files.
	'''
	mypath = os.path.join(os.getcwd(), 'test5/')
	if not os.path.isdir(mypath):
		os.mkdir(mypath)
	f = open(mypath+str('hello56'+'.txt'),'w')
	f.close()
		#create files in directory
	for i in range(100):
		f = open(mypath+str(str(i)+'bye'+'.txt'),'w')
		f.close()
		f = open(mypath+str(str(i)+'what'+'.txt'),'w')
		f.close()
		f = open(mypath+str(str(i)+'ok'+'.txt'),'w')
		f.close()
		f = open(mypath+str(str(i)+'hasta'+'.txt'),'w')
		f.close()
		f = open(mypath+str(str(i)+'lavista'+'.txt'),'w')
		f.close()
	files = file_search(mypath,'hello')
	print(files)


def user_input():
	mypath = input("Enter directory to search: ") # find directory desired
	#criteria = raw_input("")
	regex = input("Enter regex to search: ")
	file_search(os.path.join(os.getcwd(), mypath+'/'),regex)

test5()
