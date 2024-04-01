import sys

def cat():
	print('Meow!')
def defult():
	print('hello')

def main():
	if sys.argv[1] == 'cat':
		cat()
	else:	
		defult()
	
if __name__ == '__main__':
	main()
