import os
from os import listdir
from os.path import isfile, join

#function to return files with certain word in directory
def file_search(mypath, regex):
	try:
		regex_files = [f for f in listdir(mypath) if isfile(join(mypath, f)) and regex in f]
		print("Our code found ", str(len(regex_files)), " files that match your criteria")
		return regex_files
	except FileNotFoundError:
		print('Please enter a valid directory')

def test1():
	mypath = os.path.join(os.getcwd(), 'test1/')
	if not os.path.isdir(mypath):
		os.mkdir(mypath)
	#create files in directory
	for i in range(3):
		f = open(mypath+str('hello'+str(i)+'.txt'),'w')
		f.close()
		f = open(mypath+str('bye'+str(i)+'.txt'),'w')
	files = file_search(mypath,'hello')
	print(files)

def test2():
	mypath = os.path.join(os.getcwd(), 'test2/')
	if not os.path.isdir(mypath):
		os.mkdir(mypath)
		#create files in directory
	for i in range(3):
		f = open(mypath+str('goodbye'+str(i)+'.txt'),'w')
		f.close()
		f = open(mypath+str('bye'+str(i)+'.txt'),'w')
	files = file_search(mypath,'hello')
	print(files)

def test3():
	mypath = ''
	files = file_search(mypath,'hello')
	print(files)


def user_input():
	mypath = raw_input("Enter directory to search: ") # find directory desired
	#criteria = raw_input("")
	regex = raw_input("Enter regex to search: ")
	file_search(os.path.join(os.getcwd(), mypath),regex)

test3()
