import sys

def dog():
	print(' Woof!')

def defult():
	print('hello')

def main():
	if sys.argv[1] == 'dog':
		dog()
	else:
		defult()

if __name__ == '__main__':
	main()
